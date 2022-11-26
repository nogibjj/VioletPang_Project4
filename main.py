import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum


class Cities(BaseModel):
    country: str
    city: str
    type: str
    necessary_items: str


CITIES_FILE = "cities.json"
CITIES = []

if os.path.exists(CITIES_FILE):
    with open(CITIES_FILE, "r") as f:
        CITIES = json.load(f)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Welcome to my travelist app!"}


@app.get("/random-place")
async def random_cities():
    return random.choice(CITIES)


@app.get("/list-cities")
async def list_cities():
    return {"cities": CITIES}

@app.post("/add-city")
async def add_(newcity: Cities):
    newcity.city = str()
    json_city = jsonable_encoder(newcity)
    CITIES.append(json_city)

    with open(CITIES_FILE, "w") as f:
        json.dump(CITIES, f)

    return {"city": newcity.city}


@app.get("/get-city")
async def get_city(cityname: str):
    for c in CITIES:
        if c.city == cityname:
            return c

    raise HTTPException(404, f"City {cityname} not found in database.")