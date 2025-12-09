from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, HttpUrl
from typing import Optional

from app.services.pdf_service import pdf_service


router = APIRouter()


# ============== Pydantic Models ==============

class HTMLToPDFRequest(BaseModel):
    """Request body for HTML to PDF conversion."""
    html_content: str
    filename: Optional[str] = "document.pdf"
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "html_content": "<h1>Hello World</h1><p>This is a PDF generated from HTML.</p>",
                    "filename": "my-document.pdf"
                }
            ]
        }
    }


class URLToPDFRequest(BaseModel):
    """Request body for URL to PDF conversion."""
    url: HttpUrl
    filename: Optional[str] = "webpage.pdf"
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://example.com",
                    "filename": "example-page.pdf"
                }
            ]
        }
    }


class InvoiceItem(BaseModel):
    """Single item in an invoice."""
    description: str
    quantity: int = 1
    price: float


class InvoiceRequest(BaseModel):
    """Request body for invoice generation."""
    invoice_number: str
    company_name: str
    company_address: str
    client_name: str
    client_address: str
    items: list[InvoiceItem]
    currency: Optional[str] = "USD"
    notes: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "invoice_number": "INV-001",
                    "company_name": "My Company Ltd.",
                    "company_address": "123 Business Street, City, Country",
                    "client_name": "Client ABC",
                    "client_address": "456 Client Avenue, Town, Country",
                    "items": [
                        {"description": "Web Development", "quantity": 1, "price": 500.00},
                        {"description": "Consulting Hours", "quantity": 10, "price": 50.00}
                    ],
                    "currency": "USD",
                    "notes": "Payment due within 30 days."
                }
            ]
        }
    }


# ============== Endpoints ==============

@router.post("/from-html", summary="Convert HTML to PDF")
async def html_to_pdf(request: HTMLToPDFRequest):
    """
    Convert HTML content to a PDF file.
    
    - **html_content**: The HTML string to convert
    - **filename**: Optional filename for the downloaded PDF
    
    Returns the PDF file directly.
    """
    try:
        pdf_bytes = pdf_service.html_to_pdf(request.html_content)
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{request.filename}"'
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")


@router.post("/from-url", summary="Capture URL as PDF")
async def url_to_pdf(request: URLToPDFRequest):
    """
    Capture a webpage and convert it to PDF.
    
    - **url**: The URL to capture
    - **filename**: Optional filename for the downloaded PDF
    
    Returns the PDF file directly.
    """
    try:
        pdf_bytes = await pdf_service.url_to_pdf(str(request.url))
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{request.filename}"'
            }
        )
    except httpx.HTTPError as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")


@router.post("/invoice", summary="Generate Invoice PDF")
async def generate_invoice(request: InvoiceRequest):
    """
    Generate a professional invoice PDF.
    
    - **invoice_number**: Unique invoice identifier
    - **company_name**: Your company name
    - **company_address**: Your company address
    - **client_name**: Client/customer name
    - **client_address**: Client address
    - **items**: List of items with description, quantity, and price
    - **currency**: Currency code (default: USD)
    - **notes**: Optional notes or observations
    
    Returns the invoice PDF file directly.
    """
    try:
        items_dict = [item.model_dump() for item in request.items]
        
        pdf_bytes = pdf_service.generate_invoice(
            invoice_number=request.invoice_number,
            company_name=request.company_name,
            company_address=request.company_address,
            client_name=request.client_name,
            client_address=request.client_address,
            items=items_dict,
            currency=request.currency,
            notes=request.notes
        )
        
        filename = f"invoice-{request.invoice_number}.pdf"
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating invoice: {str(e)}")
