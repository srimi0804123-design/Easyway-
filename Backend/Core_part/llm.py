import ollama

def llm_extract(text: str) -> str:
    prompt = f"""
You are an expense extraction engine.

Rules:
- Return ONLY valid JSON
- No markdown
- No explanations outside JSON
- EXACT keys only

Keys:
amount, merchant, category, date, payment_mode, confidence, reasoning

Categories:
Food, Travel, Groceries, Shopping, Utilities, Education, Entertainment, Other

IMPORTANT:
- Ignore individual item lines and tables.
- Focus ONLY on total amount, merchant name, date, and payment mode.
- Do NOT attempt to extract itemized details.
- If total amount is unclear, set amount = 0.


If amount is missing or unclear, set confidence <= 0.4

Input:
{text}
"""

    response = ollama.generate(
        model="mistral",
        prompt=prompt,
        options={"temperature": 0}
    )

    return response["response"].strip()
