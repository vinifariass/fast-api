# PDF Generator API

A RESTful API for generating professional PDFs from HTML, URLs, and templates.

## 🚀 Quick Start

### 1. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn app.main:app --reload
```

### 4. Access documentation
Open: http://localhost:8000/docs

---

## 📖 Endpoints

### POST /pdf/from-html
Converts HTML to PDF.

**Request:**
```json
{
  "html_content": "<h1>Hello World</h1><p>This is a PDF</p>",
  "filename": "document.pdf"
}
```

**Response:** PDF file download

---

### POST /pdf/from-url
Captures a webpage as PDF.

**Request:**
```json
{
  "url": "https://example.com",
  "filename": "website.pdf"
}
```

**Response:** PDF file download

---

### POST /pdf/invoice
Generates a professional invoice.

**Request:**
```json
{
  "invoice_number": "INV-001",
  "company_name": "My Company",
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
```

**Response:** Invoice PDF file download

---

## 💰 Pricing Plans

| Plan | Price | PDFs/month |
|------|-------|------------|
| Free | $0 | 10 |
| Basic | $5 | 100 |
| Pro | $15 | 500 |
| Business | $50 | 5000 |

---

## 🐳 Deploy with Docker

```bash
docker build -t pdf-api .
docker run -p 8000:8000 pdf-api
```

---

## 📄 License

MIT License
