from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

import json
from pathlib import Path

# Lade Unternehmensdatenbank beim Start
companies_file = Path("companies.json")
if companies_file.exists():
    with open(companies_file, "r", encoding="utf-8") as f:
        companies_data = json.load(f)
else:
    companies_data = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CultureFitInput(BaseModel):
    taskDesign: str
    changeHandling: str
    errorCulture: str
    purpose: str
    performancePressure: str
    activities: str
    experiences: str

class CompanyRecommendation(BaseModel):
    name: str
    description: str

@app.post("/api/analyse-user-profile")
async def analyse(user_input: CultureFitInput):
    print("Erhaltene Eingaben:", user_input.dict())

    dummy_results = [
        CompanyRecommendation(name="Innovate GmbH", description="Technologie-Startup mit Fokus auf KI."),
        CompanyRecommendation(name="GreenFuture AG", description="Nachhaltige Lösungen für die Energiebranche.")
    ]
    return { "companies": dummy_results }

