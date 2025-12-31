import json
from datetime import date
import ollama  #Locally used LLM - Mistral


def extract_expense(text: str) -> dict:
    prompt = f"""
You are an expense extraction engine.

Extract structured expense data from the input text.

Rules:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations outside JSON
- Do NOT add extra keys

The JSON must have EXACTLY these keys:
- amount (number)
- merchant (string)
- category (string)
- date (string in YYYY-MM-DD format or "Unknown")
- payment_mode (string)
- confidence (number between 0 and 1)
- reasoning (short string)

Allowed categories:
Food, Travel, Groceries, Shopping, Utilities, Education, Entertainment, Other

If information is unclear:
- Make a reasonable guess
- Lower the confidence score


Input text:
{text}
"""

    try:
        response = ollama.generate(
            model="mistral",
            prompt=prompt,
            options={
                "temperature": 0
            }
        )

        raw_output = response["response"].strip()

    except Exception as e: #When a error occures instead of showing error its shows this
        return {
            "amount": 0,
            "merchant": "Unknown",
            "category": "Other",
            "date": "Unknown",
            "payment_mode": "Unknown",
            "confidence": 0.0,
            "reasoning": f"Ollama request failed: {str(e)[:100]}"
        }

    try:
        expense_data = json.loads(raw_output)

    except json.JSONDecodeError:
        expense_data = {
            "amount": 0,
            "merchant": "Unknown",
            "category": "Other",
            "date": date.today().isoformat(),
            "payment_mode": "Unknown",
            "confidence": 0.0,
            "reasoning": "Failed to parse LLM output"
        }

    if expense_data["date"] == "Unknown": #If the date is now extracted from the given info
        expense_data["date"] = date.today().isoformat() #It replaces it from that day's date
        expense_data["reasoning"] += " | Date defaulted to today"

    return expense_data

