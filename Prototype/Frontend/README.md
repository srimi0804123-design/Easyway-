# EasyWay – Frontend (Streamlit)

EasyWay is a simple **AI-based expense tracker for Indian students**. This frontend is built using **Streamlit** and connects to a FastAPI backend to extract expense details from text or images.

---

## Features

* Enter expense details as text (UPI / bill message)
* Upload bill or UPI screenshots
* Shows extracted expense details clearly
* Easy-to-use Streamlit UI

---

## Tech Used

* Streamlit (Frontend)
* Python
* FastAPI Backend (API)

---

## Project Files

```
app.py
requirements.txt
README.md
```

---

## How to Run Frontend

### Step 1: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 2: Run Streamlit App

```bash
streamlit run app.py
```

App will open in browser at:

```
http://localhost:8501
```

---

## Backend Connection

Frontend sends data to backend using this URL in `app.py`:

```python
BACKEND_URL = "http://127.0.0.1:8000/parse-expense"
```

If backend is deployed, replace it with your live backend URL.

---

## How It Works

1. Choose input type: Text or Image
2. Enter text or upload image
3. Click **Extract Expense**
4. View extracted details like amount, merchant, category, etc.

---

## Common Issue

**Backend not connecting?**

* Make sure backend is running
* Check backend URL

---

## Author

Anshika Gaur

---

## Note

This project is made for learning / hackathon purposes.
