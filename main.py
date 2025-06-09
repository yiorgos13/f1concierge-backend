
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import datetime
import random

app = FastAPI()

F1_RACES = [
    {"id": 1, "name": "Miami GP", "location": "Miami", "date": "2025-05-04"},
    {"id": 2, "name": "United States GP", "location": "Austin", "date": "2025-10-19"},
    {"id": 3, "name": "Las Vegas GP", "location": "Las Vegas", "date": "2025-11-22"}
]

ORIGINS = [
    "New York (JFK)", "London (LHR)", "Tokyo (NRT)", "Paris (CDG)", "Dubai (DXB)"
]

class PriceRequest(BaseModel):
    race_id: int
    origin_city: str

class PriceResponse(BaseModel):
    race: str
    origin: str
    flight_price: float
    hotel_price: float
    ticket_price: float
    checked_at: str

@app.get("/races", response_model=List[dict])
def list_races():
    return F1_RACES

@app.get("/origins", response_model=List[str])
def list_origins():
    return ORIGINS

@app.post("/price-check", response_model=PriceResponse)
def check_price(req: PriceRequest):
    race = next((r for r in F1_RACES if r["id"] == req.race_id), None)
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    if req.origin_city not in ORIGINS:
        raise HTTPException(status_code=400, detail="Invalid origin city")

    flight = round(random.uniform(300, 900), 2)
    hotel = round(random.uniform(200, 450), 2)
    ticket = round(random.uniform(350, 700), 2)

    return PriceResponse(
        race=race["name"],
        origin=req.origin_city,
        flight_price=flight,
        hotel_price=hotel,
        ticket_price=ticket,
        checked_at=datetime.datetime.utcnow().isoformat()
    )
