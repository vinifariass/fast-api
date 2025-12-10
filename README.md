# PDF Generator API

🔥 A powerful, affordable API for generating professional PDFs from HTML, URLs, and templates.

## ✨ Why Choose This API?

- ✅ **30% cheaper** than competitors (Api2Pdf, PDF.co)
- ✅ **Ready-to-use invoice templates** - exclusive feature!
- ✅ **Simple pricing** - no confusing credit system
- ✅ **Fast & reliable** - modern infrastructure

---

## 💰 Pricing

| Plan | Price | PDFs/month | Cost per PDF |
|------|-------|------------|--------------|
| **Free** | $0 | 50 | - |
| **Basic** | $5 | 200 | $0.025 |
| **Pro** | $12 | 1,000 | $0.012 |
| **Business** | $29 | 5,000 | $0.006 |

---

## 🚀 Quick Start

### Installation
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Run
```bash
uvicorn app.main:app --reload
```

### Documentation
Open: http://localhost:8000/docs

---

## 📖 Endpoints

### POST /pdf/from-html
Converts HTML to PDF.

```json
{
  "html_content": "<h1>Hello World</h1><p>This is a PDF</p>",
  "filename": "document.pdf"
}
```

### POST /pdf/from-url
Captures a webpage as PDF.

```json
{
  "url": "https://example.com",
  "filename": "website.pdf"
}
```

### POST /pdf/invoice
Generates a professional invoice.

```json
{
  "invoice_number": "INV-001",
  "company_name": "My Company",
  "company_address": "123 Business Street",
  "client_name": "Client ABC",
  "client_address": "456 Client Avenue",
  "items": [
    {"description": "Web Development", "quantity": 1, "price": 500.00},
    {"description": "Consulting", "quantity": 10, "price": 50.00}
  ],
  "currency": "USD",
  "notes": "Payment due within 30 days."
}
```

---

## 🐳 Deploy

```bash
docker build -t pdf-api .
docker run -p 8000:8000 pdf-api
```

---

## 📄 License

MIT License
