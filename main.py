from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    answers: Dict[str, str]

@app.post("/api/analyse-user-profile")
async def analyse(user_input: UserInput):
    dummy_results = [
        {
            "company": "Innovate Solutions GmbH",
            "description": "Führend in KI-gestützter Prozessautomatisierung.",
            "tags": ["Innovativ", "Datengesteuert", "Agil"]
        },
        {
            "company": "Grünwerk AG",
            "description": "Nachhaltige Technologien für eine bessere Zukunft.",
            "tags": ["Sinnstiftend", "Umweltbewusst", "Teamorientiert"]
        }
    ]
    return { "companies": dummy_results }
