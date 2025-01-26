# main.py - Example FastAPI application

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict_fraud(data: dict):
    return {
        "transaction_id": data.get("transaction_id"),
        "is_fraud": True,
        "fraud_probability": 0.85
    }
