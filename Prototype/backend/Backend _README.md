# EasyWay Backend

A Python backend prototype that extracts structured expense information from **text input or receipt/UPI screenshots** using OCR and a **local LLM (Mistral via Ollama)**.

This project focuses only on the backend logic and AI pipeline.

---

## Features

* Accepts plain text expense descriptions.
* Accepts images of receipts or UPI payment screenshots.
* Uses OCR to extract raw text from images.
* Uses a local LLM (Mistral) to infer expense details.
* Returns structured JSON output with confidence and reasoning.
* Graceful fallback handling when OCR or LLM fails.

---

## Requirements

* Python 3.10+
* Ollama installed and running
* Mistral model pulled in Ollama
* Tesseract OCR installed (system dependency)

### Python Libraries Used

* `fastapi`
* `uvicorn`
* `pytesseract`
* `pillow`
* `python-dotenv`
* `python-multipart`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Backend Workflow
```
POST /parse-expense
        |
        |-- if image file is provided
        |       |
        |       |-- OCR (Tesseract)
        |       |-- extracted raw text
        |
        |-- if text is provided
        |       |
        |       |-- raw text
        |
        |-- LLM reasoning (Mistral via Ollama)
        |
        |-- structured JSON response
```

## API Endpoint
>**POST /parse-expense**
```Input (multipart/form-data)
text : string (optional)
file : image (optional)
```

>Output (JSON)
```
{
  "amount": 59,
  "merchant": "Local Shop",
  "category": "Food",
  "date": "2025-01-01",
  "payment_mode": "Cash",
  "confidence": 0.82,
  "reasoning": "Amount inferred from text. Category inferred from keyword 'snacks'."
}
```

## How to Run

>**Start the backend server:**
```
uvicorn backend.main:app --reload
```

>**Open API documentation at:**
```
http://127.0.0.1:8000/docs
```

## Limitations

* OCR accuracy depends on image quality.
* No database or persistent storage.
* No authentication or user management.
* Prototype-only, not production-ready.
