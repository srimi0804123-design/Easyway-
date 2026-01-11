from Core_part.llm import llm_extract
from Core_part.validate import validate_llm_output
from Core_part.normalizing import normalize_expense
from schemas.expense_schema import DEFAULT_EXPENSE


def extract_expense(text: str, source: str = "manual") -> dict:
    try:
        raw_output = llm_extract(text)
        data = validate_llm_output(raw_output)

        if data is None:
            raise ValueError("Validation failed")

        return normalize_expense(data, source)

    except Exception as e:
        return {
            "amount": 0,
            "merchant": "Unknown",
            "category": "Other",
            "date": "Unknown",
            "payment_mode": "Unknown",
            "confidence": 0.0,
            "reasoning": f"Pipeline failure: {str(e)[:80]}"
        }

