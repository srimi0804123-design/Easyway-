# EASY WAY 

### AI-Powered Expense Tracker for Students

## Overview

**EASY WAY** is an intelligent expense tracking and budget management system built using **Artificial Intelligence (AI)** and **Machine Learning (ML)**. It automatically extracts expense details from **bills, receipts, and UPI screenshots**, then converts them into structured data to help users understand and manage their spending.

The goal is simple:
make expense tracking **effortless**, **automatic**, and **not boring**.

---

## Problem Statement

Most students:

* Rely heavily on **UPI and cash** for daily transactions
* Rarely track expenses consistently
* Avoid budgeting because it feels tedious
* Never analyze bills beyond “money gone, pain remains”

Manual expense tracking fails because it depends on discipline.
This project improves expense categorization accuracy by learning from user-specific transaction patterns rather than relying only on vendor names.

---

## Solution

**EASY WAY** automates expense analysis using AI.

### How it works:

1. User uploads a **bill image**, **UPI screenshot**, or enters **text/voice input**
2. The frontend sends data to the backend via API
3. **OCR** extracts raw text from images
4. A **local LLM** interprets the text and identifies expense details
5. Structured expense data is returned
6. Insights are displayed instantly on the frontend

No spreadsheets. No mental math. No regret later.

---

## Key Features

* Upload receipts, bills, or UPI screenshots
* Enter expenses using plain text
* AI automatically extracts:

  * Amount
  * Merchant
  * Date
  * Category
  * Payment mode
* Expenses are categorized intelligently
* Confidence score included for transparency
* Optional voice-based input for cash expenses (planned)

---
## What Makes EASY WAY Different?

EASY WAY is built for real-world UPI usage, where transaction screenshots contain noisy OCR data and vendor names are often personal rather than business identifiers.

- Uses **OCR** to extract payment details from UPI screenshots, even when the data is incomplete or messy  
- Applies a **Large Language Model (LLM)** as a reasoning layer to interpret transactions instead of relying on rigid rule-based systems  
- Learns from **user corrections** to build personalized expense categorization over time  
- Assigns a **confidence score** to each prediction, requesting user input only when uncertainty is high


## Tech Stack

### Frontend

* **Streamlit** (Prototype UI)
* Lightweight, mobile-friendly interface
* Supports:

  * Image upload
  * Text-based expense entry
* Communicates with backend via REST API

**Focus:**
Minimum friction for user input

---

### Backend

* **Python + FastAPI**
* Handles:

  * API requests
  * OCR processing
  * LLM-based reasoning
  * Structured JSON responses

**Focus:**
Speed, simplicity, and clean data flow

---

## AI Processing Layer

### OCR (Optical Character Recognition)

* Extracts text from uploaded images
* Handles printed and semi-structured receipts
* Powered by **Tesseract OCR**

### Large Language Model (LLM)

* Local **Mistral model** via **Ollama**
* Interprets unstructured text
* Infers missing or unclear information
* Converts raw text into structured expense data
* Assigns confidence scores

**Design Philosophy:**
Interpretation over rigid rules.

---

## Database

* **MongoDB** (Planned)
* Not used in the current prototype
* Chosen for:

  * Flexible document structure
  * Scalability
  * Efficient handling of large expense datasets

---

## Tools & Development Environment

* **Git** – Version control
* **GitHub** – Repository hosting and collaboration
* **Visual Studio Code** – Primary development environment

---

## System Workflow

1. User submits expense input
2. Frontend sends request to FastAPI backend
3. Backend processes input:

   * OCR (if image)
   * LLM reasoning
4. Structured expense data is generated
5. Results are returned and displayed

## System Main Flowchart

![Main flowchart](flowchart/main_flowchart.jpg)

## AI Processing Flow
![AI_flow](flowchart/AI_processing_layers.jpg)

---
## Demo Prototype
* Input Text
![Input_Text](Prototype/Images/input_text.png)
* Extracted Details
![output](Prototype/Images/output(text).png)
* Upload bill/UPI Screenshot
![UPI_sample](Prototype/Images/UPI_sample.png)
* Extracted Details
![output](Prototype/Images/output(UPI).png)

---
## Backend API

### Endpoint

**POST `/parse-expense`**

#### Input (multipart/form-data)

* `text` (optional)
* `file` (optional – image)

#### Output (JSON)

```json
{
  "amount": 59,
  "merchant": "Local Shop",
  "category": "Food",
  "date": "2025-01-01",
  "payment_mode": "Cash",
  "confidence": 0.82,
  "reasoning": "Amount inferred from text. Category inferred from keyword."
}
```

---

## How to Run the Project

### Backend

```bash
uvicorn backend.main:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
streamlit run app.py
```

---

## Limitations

* OCR accuracy depends on image quality
* No persistent storage (yet)
* No authentication or multi-user support
* Prototype-level implementation, not production-ready

---

## Future Enhancements

1. Monthly spending analysis and behavioral insights
2. Overspending prediction and alerts
3. MongoDB integration for persistent storage
4. Multi-user support
5. Social or shared expense features

---

## Authors

* **Swastika Mukherjee**
* **Priyanshi Tamta**
* **Vanshika Maheshwari**
* **Anshika Gaur**

---

## Credits

* **Vanshika Maheshwari** – Full Stack AI Development
* **Anshika Gaur** – Frontend Development
* **Priyanshi Tamta** – Documentation & Project Management
* **Swastika Mukherjee** – Overall Contribution
