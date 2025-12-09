from io import BytesIO
from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
import httpx

from app.config import TEMPLATES_DIR


class PDFService:
    """Service for generating PDFs."""
    
    def __init__(self):
        # Setup Jinja2 template environment
        self.template_env = Environment(
            loader=FileSystemLoader(TEMPLATES_DIR)
        )
    
    def html_to_pdf(self, html_content: str) -> bytes:
        """
        Convert HTML content to PDF.
        
        Args:
            html_content: HTML string to convert
        
        Returns:
            PDF as bytes
        """
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
        
        if pisa_status.err:
            raise Exception("Error generating PDF")
        
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()
    
    async def url_to_pdf(self, url: str) -> bytes:
        """
        Capture a URL as PDF.
        
        Args:
            url: URL to capture
        
        Returns:
            PDF as bytes
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()
            html_content = response.text
        
        return self.html_to_pdf(html_content)
    
    def generate_invoice(
        self,
        invoice_number: str,
        company_name: str,
        company_address: str,
        client_name: str,
        client_address: str,
        items: list,
        currency: str = "USD",
        notes: str = None
    ) -> bytes:
        """
        Generate a professional invoice PDF.
        
        Args:
            invoice_number: Invoice number/ID
            company_name: Your company name
            company_address: Your company address
            client_name: Client/customer name
            client_address: Client address
            items: List of items with description, quantity, price
            currency: Currency code (USD, BRL, EUR, etc.)
            notes: Optional notes/observations
        
        Returns:
            PDF as bytes
        """
        # Calculate totals
        subtotal = sum(item["quantity"] * item["price"] for item in items)
        
        # Load and render template
        template = self.template_env.get_template("invoice.html")
        html_content = template.render(
            invoice_number=invoice_number,
            company_name=company_name,
            company_address=company_address,
            client_name=client_name,
            client_address=client_address,
            items=items,
            subtotal=subtotal,
            total=subtotal,
            currency=currency,
            notes=notes
        )
        
        return self.html_to_pdf(html_content)


# Singleton instance
pdf_service = PDFService()
