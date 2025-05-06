from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

app = FastAPI()

# CORS-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Produktion später auf spezifische Domains einschränken
    allow_methods=["*"],
    allow_headers=["*"],
)

# Eingabemodell vom Frontend
class CultureFitInput(BaseModel):
    taskDesign: str
    changeHandling: str
    errorCulture: str
    purpose: str
    performancePressure: str
    activities: str
    experiences: str

# Ausgabemodell für die Empfehlungen
class CompanyRecommendation(BaseModel):
    name: str
    description: str

# Lade die Unternehmensdatenbank aus JSON-Datei
companies_file = Path("companies.json")
if companies_file.exists():
    with open(companies_file, "r", encoding="utf-8") as f:
        companies_data = json.load(f)
else:
    companies_data = []

@app.post("/api/analyse-user-profile")
async def analyse(user_input: CultureFitInput):
    print("Eingaben erhalten:", user_input.dict())

    # TODO: Hier später semantisches Matching mit `user_input` gegen `companies_data`

    # Aktuell: Gib einfach die ersten 3 Firmen zurück als Platzhalter
    dummy_results = companies_data[:3]

    return {"companies": dummy_results}

