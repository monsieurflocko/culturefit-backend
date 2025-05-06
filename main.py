from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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

