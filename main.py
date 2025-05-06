from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

# CORS-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Produktion später auf spezifische Domains einschränken
    allow_credentials=True,
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

# Initialisiere das Embedding-Modell
model = SentenceTransformer("all-MiniLM-L6-v2")

# Erstelle Embeddings für alle Unternehmensbeschreibungen
company_descriptions = [company["description"] for company in companies_data]
company_embeddings = model.encode(company_descriptions, convert_to_tensor=True)

@app.post("/api/analyse-user-profile")
async def analyse(user_input: CultureFitInput):
    print("Eingaben erhalten:", user_input.dict())

    # Kombiniere die Nutzereingaben zu einem Text
    user_text = " ".join([
        user_input.taskDesign,
        user_input.changeHandling,
        user_input.errorCulture,
        user_input.purpose,
        user_input.performancePressure,
        user_input.activities,
        user_input.experiences
    ])

    # Erzeuge Embedding für die Nutzereingabe
    user_embedding = model.encode(user_text, convert_to_tensor=True)

    # Berechne Cosine Similarity zwischen Nutzerprofil und allen Unternehmensbeschreibungen
    similarities = cosine_similarity(
        user_embedding.cpu().numpy().reshape(1, -1),
        company_embeddings.cpu().numpy()
    )[0]

    # Finde die Top 3 ähnlichsten Unternehmen
    top_indices = np.argsort(similarities)[::-1][:3]
    top_companies = [companies_data[i] for i in top_indices]

    return {"companies": top_companies}
