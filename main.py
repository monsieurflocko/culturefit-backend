from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    answers: Dict[str, str]

class CompanyRecommendation(BaseModel):
    name: str
    description: str

@app.post("/api/analyse-user-profile")
async def analyse(user_input: UserInput):
    dummy_results = [
        CompanyRecommendation(
            name="Innovate Solutions GmbH",
            description="Führend in KI-gestützter Prozessautomatisierung."
        ),
        CompanyRecommendation(
            name="Grünwerk AG",
            description="Nachhaltige Technologien für eine bessere Zukunft."
        )
    ]
    return { "companies": dummy_results }
