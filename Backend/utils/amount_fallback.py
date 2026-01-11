import re

def extract_amount_fallback(text: str) -> float | None:
    patterns = [
        r"₹\s*([0-9]+(?:\.[0-9]{1,2})?)",
        r"Rs\.?\s*([0-9]+(?:\.[0-9]{1,2})?)",
        r"INR\s*([0-9]+(?:\.[0-9]{1,2})?)",
        r"TOTAL\s*[:\-]?\s*₹?\s*([0-9]+(?:\.[0-9]{1,2})?)",
        r"Total\s*[:\-]?\s*([0-9]+(?:\.[0-9]{1,2})?)",
    ]

    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except:
                pass

    return None
