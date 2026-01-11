import json
from schemas.expense_schema import (
    REQUIRED_KEYS,
    ALLOWED_CATEGORIES,
    ALLOWED_PAYMENT_MODES,
    MIN_CONFIDENCE,
    MAX_CONFIDENCE,
)

def validate_llm_output(raw_output: str) -> dict | None:
    try:
        data = json.loads(raw_output)
    except Exception:
        return None

    # --- Key presence ---
    for key in REQUIRED_KEYS:
        if key not in data:
            return None

    # --- Type normalization ---
    try:
        data["amount"] = float(data.get("amount", 0))
    except Exception:
        data["amount"] = 0.0

    try:
        data["confidence"] = float(data.get("confidence", 0))
    except Exception:
        data["confidence"] = 0.0

    # --- String safety ---
    for k in ["merchant", "category", "date", "payment_mode", "reasoning"]:
        data[k] = str(data.get(k, "Unknown")).strip() or "Unknown"

    # --- Category normalization ---
    if data["category"] not in ALLOWED_CATEGORIES:
        data["category"] = "Other"
        data["confidence"] *= 0.7

    # --- Payment mode normalization ---
    if data["payment_mode"] not in ALLOWED_PAYMENT_MODES:
        data["payment_mode"] = "Unknown"

    # --- Confidence clamp ---
    data["confidence"] = max(
        MIN_CONFIDENCE,
        min(MAX_CONFIDENCE, data["confidence"])
    )

    return data
