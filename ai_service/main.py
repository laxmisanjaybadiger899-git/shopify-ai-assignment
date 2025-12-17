from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    store_id: str
    question: str

@app.post("/analyze")
def analyze_question(data: QuestionRequest):
    question = data.question.lower()

    # Step 1: Intent detection (mock LLM)
    if "inventory" in question or "reorder" in question:
        intent = "inventory"
    elif "sales" in question:
        intent = "sales"
    else:
        intent = "unknown"

    # Step 2: Mock ShopifyQL + logic
    if intent == "inventory":
        avg_daily_sales = 10
        reorder_qty = avg_daily_sales * 7

        answer = (
            "Based on the last 30 days, you sell around "
            f"{avg_daily_sales} units per day. "
            f"You should reorder at least {reorder_qty} units "
            "to avoid stockouts next week."
        )
        confidence = "medium"
    else:
        answer = "I could not clearly understand the question."
        confidence = "low"

    return {
        "store_id": data.store_id,
        "intent_detected": intent,
        "answer": answer,
        "confidence": confidence
    }
