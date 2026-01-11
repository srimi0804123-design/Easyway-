# EasyWay – Backend

## Overview

The **EasyWay Backend** is a FastAPI-based service that powers an AI-driven expense extraction and categorization system.  
It processes raw text or OCR-extracted text from payment screenshots (UPI, receipts, bills) and converts it into structured expense data using OCR and Large Language Models (LLMs).

This backend is designed to be **modular**, **scalable**, and suitable for hackathon evaluation as well as future production deployment.

---

## Tech Stack

### Core
- **Python** `3.10+`
- **FastAPI** `0.110.0`
- **Uvicorn** `0.29.0`

### Data & Validation
- **Pydantic** `2.6.4`
- **python-multipart** `0.0.9`

### OCR & Image Processing
- **pytesseract** `0.3.10`
- **Pillow (PIL)** `10.2.0`

### AI / LLM
- **openai** `1.12.0` *(or compatible LLM API)*

### Utilities
- **python-dotenv** `1.0.1`
- **requests** `2.31.0`

---

## Core Modules

### 1. OCR Module
- Extracts raw text from payment screenshots, receipts, and bills
- Built using **Pytesseract**
- Handles noisy images and inconsistent layouts
- Outputs unstructured text for further processing

---

### 2. LLM Module
- Uses a Large Language Model to interpret extracted text
- Identifies and structures:
  - Amount
  - Merchant name
  - Expense category
  - Date
  - Payment mode
  - Confidence score
- Designed to handle semi-structured and unstructured payment text

---

### 3. Main Pipeline Module
- Acts as the **connector** between OCR and LLM modules
- Orchestrates the full flow:
  1. OCR text extraction
  2. Text cleaning and preprocessing
  3. LLM-based information extraction
- Returns structured expense data to the API layer

## Setup Instructions

###  Clone the Repository
```bash
git clone <repository-url>
cd Easyway-/Backend
```
###  Create and Activate Virtual Environment
```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

```
### Install Python Dependencies
```bash
pip install -r requirements.txt
```
### Run the Backend Server
```bash
uvicorn main:app --reload
```
### Access API Documentation
```bash
uvicorn main:app --reload
```
- Backend Server
```bash
http://127.0.0.1:8000
```
-Interactive API Docs
```bash
http://127.0.0.1:8000/docs
```
##  Future Enhancements

### 1. Database Integration
- Store structured expense data persistently
- Enable user-wise expense history
- Possible databases:
  - PostgreSQL (relational, structured analytics)
  - MongoDB (flexible schema for OCR variability)

---

### 2. User Authentication & Profiles
- Secure user accounts
- Expense tracking per user
- JWT-based authentication for API access

---

### 3. Improved OCR Accuracy
- Image preprocessing (denoising, thresholding)
- Support for low-resolution and dark-mode screenshots
- OCR confidence scoring

---

### 4. LLM Optimization
- Fine-tuning or prompt optimization for UPI-specific formats
- Reduced hallucinations and improved consistency
- Cost and latency optimization

---

### 5. Multi-language Support
- OCR support for regional languages
- Language detection before LLM processing
- Better accessibility for non-English users

---

### 6. Confidence-Based Validation
- Flag low-confidence extractions
- Allow manual correction by users
- Feedback loop to improve extraction accuracy

---

### 7. Analytics & Insights
- Monthly spending summaries
- Category-wise expense breakdown
- Visual analytics for frontend integration

---

### 8. Scalability & Deployment
- Containerization using Docker
- Cloud deployment (AWS / GCP / Azure)
- Asynchronous processing for high-volume uploads
