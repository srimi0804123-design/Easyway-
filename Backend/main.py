from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from Core_part import extract_expense
from OCR_part import extract_text_from_image
from utils.amount_fallback import extract_amount_fallback

app = FastAPI(title="Expense Extraction API")




# CORS (needed for web frontend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Checks if the backend is working

@app.get("/")
def health_check():
    return {"status": "Backend is running"}

#Text-based Expense Parsing

@app.post("/parse-expense")
def parse_expense(
    text: str = Form(...),
    source: str = Form("manual")
):
    """
    Handles manual or voice-based expense input.
    """
    return extract_expense(text=text, source=source)

# OCR-based Expense Parsing 

@app.post("/parse-expense-image")
async def parse_expense_image(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Prototype OCR (string only)
    text = extract_text_from_image(image_bytes)

    # Always pass to LLM (prototype behavior)
    expense = extract_expense(text=text, source="ocr")

    # Optional: light honesty tag
    expense["reasoning"] += " | OCR-based inference"

    return expense
