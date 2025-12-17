from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI service is running"}

@app.post("/analyze")
def analyze_text(query: Query):
    # Fake AI logic (simple for assignment)
    result = query.text.upper()
    return {
        "original_text": query.text,
        "ai_result": result
    }
