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
* **Invoices**: Generate professional invoices and receipts (exclusive feature!)

## Why Choose Us?

✅ **30% cheaper** than competitors  
✅ **Ready-to-use invoice templates** (others don't have this!)  
✅ **Simple pricing** - no confusing credit system  
✅ **Fast response** - powered by modern infrastructure

## Pricing

| Plan | Price | PDFs/month | Cost per PDF |
|------|-------|------------|--------------|
| **Free** | $0 | 50 | - |
| **Basic** | $5 | 200 | $0.025 |
| **Pro** | $12 | 1,000 | $0.012 |
| **Business** | $29 | 5,000 | $0.006 |

💰 **Save 30%** compared to Api2Pdf and other alternatives!
"""
API_VERSION = "1.0.0"
