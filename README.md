# EASY WAY

## Overview

**EASY WAY** is a smart and efficient financial management system that uses **Artificial Intelligence (AI)** and **Machine Learning (ML)** to analyze uploaded bills and generate a personalized budget plan.

The system helps users:
- Track expenses
- Identify spending patterns
- Make data-driven financial decisions

---

## Problem Statement

- Students use UPI or cash for most transactions.
- Expense tracking is often boring and neglected.
- Users fail to analyze bills effectively.

This project automates expense analysis using AI/ML to provide intelligent and hassle-free budget tracking.

---

## Solution Overview

1. Users upload a photo of a bill or a UPI screenshot.
2. The frontend sends data to the backend via API requests.
3. OCR extracts information from the image.
4. FastAPI processes the data and runs LLM models for expense categorization.
5. Budget insights are visually displayed to the user.

---

## Key Features

- Upload bills (Image )
- AI extracts:
  - Amount
  - Merchant
  - Date
  - Category
- Expenses are automatically added to the tracker
- Optional voice note input for cash expenses

---

## Tech Stack

### Frontend

**React** (Framework of HTML, JavaScript)

Used in prototype:
- Lightweight, mobile-friendly web interface using **Streamlit**
- API communication using **Python Requests**

**Supports:**
- Image upload (receipt, bill)
- Voice input (spoken expenses)

**Focus:**  
Capture input with the least possible friction

---

### Backend

**Python-based backend using FastAPI**

**Handles:**
- Request validation
- Input routing
- AI pipeline coordination
- Response formatting

**Focus:**  
Simplicity, speed, and clear data flow

---

## AI Processing Layer

### OCR
- Extracts raw text from uploaded images
- Handles printed and semi-structured receipts

### Speech-to-Text
- Converts voice input into text for processing

### Large Language Model (LLM)
- Interprets unstructured text
- Identifies key expense details:
  - Amount
  - Merchant
  - Date
  - Category
- Normalizes inconsistent or incomplete inputs
- Converts raw data into structured format

**Focus:**  
Intelligence through interpretation, not rule-based parsing

---

## Database

**MongoDB**

- Not currently used in the prototype
- Planned for future versions to support scalability
- Flexible document-based structure
- Suitable for handling large volumes of bill and expense data

---

## Tools

- **Git** – Tracks and manages changes in source code
- **GitHub** – Hosts the project repository and enables collaboration
• **Visual Studio Code (VS Code)** is used as the primary development tool for writing, debugging, and managing the project code. It helps in productivity and efficiency of program.
-----

## System Workflow

1. User uploads bills
2. Requests are sent to the FastAPI backend
3. Backend processes the bill using rule-based logic
4. Budget details are generated and returned
5. Results are displayed on the frontend

### System Flow Block Diagram


## FURTHER SCALABILITY
* 1. A feature can be added to give monthly behavioral insights and  pridict alerts when the user is about to overspend. 
* 2.MongoDB is used for its flexible structure and ability to handle large datasets efficiently by storing them.
* 3.A Multi-user or Social Feature can be added. 
## Authors

- Swastika Mukherjee  
- Priyanshi Tamta  
- Vanshika Maheshwari  
-  Anshika Gaur

## CREDITS
*  Vanshika Maheshwari : Backend
* Anshika Gaur : Frontend
* Swastika Mukherjee
* Priyanshi Tamta: Readme.MD files and overall management
