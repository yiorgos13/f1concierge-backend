# F1 Concierge Backend

This is the backend API for the **F1 Concierge** mobile app. It provides real-time (simulated) pricing data for flights, hotels, and race tickets for F1 events.

---

## 📦 Features

- `/races` – list of supported F1 races
- `/origins` – global origin city options
- `/price-check` – returns flight, hotel, and ticket price for a given race and origin city

---

## 🛠 How to Run Locally

1. Clone this repo:

```bash
git clone https://github.com/yorogos13/f1concierge-backend.git
cd f1concierge-backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

Then visit `http://localhost:10000/docs` for the Swagger API UI.

---

## 🚀 Deploy to Render

When creating a new Web Service:

- **Language:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`

---

## 📱 Used By

This API powers the **F1 Concierge** mobile app (built with React Native + Expo).

