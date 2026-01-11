from datetime import date

def normalize_expense(data: dict, source: str = "manual") -> dict:
    if data["date"] == "Unknown":
        data["date"] = date.today().isoformat()
        data["confidence"] *= 0.8
        data["reasoning"] += " | Date defaulted to today"

    if source == "voice":
        data["confidence"] *= 0.9
        data["reasoning"] += " | Voice input"

    if source == "ocr":
        data["confidence"] *= 0.95
        data["reasoning"] += " | OCR input"

    return data
