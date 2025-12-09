import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Templates directory
TEMPLATES_DIR = BASE_DIR / "app" / "templates"

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# API Info
API_TITLE = "PDF Generator API"
API_DESCRIPTION = """
🔥 **Professional PDF Generation API**

## Features

* **HTML → PDF**: Convert any HTML code to PDF
* **URL → PDF**: Capture web pages as PDF
* **Invoices**: Generate professional invoices and receipts

## Usage

All endpoints return the PDF file directly for download.

## Pricing

| Plan | Price | PDFs/month |
|------|-------|------------|
| Free | $0 | 10 |
| Basic | $5 | 100 |
| Pro | $15 | 500 |
| Business | $50 | 5000 |
"""
API_VERSION = "1.0.0"
