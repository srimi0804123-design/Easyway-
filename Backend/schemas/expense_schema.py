from typing import Dict, Tuple, Union

# ---------- Allowed Values ----------

ALLOWED_CATEGORIES = {
    "Food",
    "Travel",
    "Groceries",
    "Shopping",
    "Utilities",
    "Education",
    "Entertainment",
    "Other"
}

ALLOWED_PAYMENT_MODES = {
    "UPI",
    "Cash",
    "Card",
    "NetBanking",
    "Wallet",
    "Unknown"
}

# ---------- Required Schema ----------

REQUIRED_KEYS: Dict[str, Tuple[type, ...]] = {
    "amount": (int, float),
    "merchant": (str,),
    "category": (str,),
    "date": (str,),
    "payment_mode": (str,),
    "confidence": (int, float),
    "reasoning": (str,)
}

# ---------- Defaults (used on failure) ----------

DEFAULT_EXPENSE = {
    "amount": 0,
    "merchant": "Unknown",
    "category": "Other",
    "date": "Unknown",
    "payment_mode": "Unknown",
    "confidence": 0.0,
    "reasoning": "Extraction failed"
}

# ---------- Confidence Bounds ----------

MIN_CONFIDENCE = 0.0
MAX_CONFIDENCE = 1.0
