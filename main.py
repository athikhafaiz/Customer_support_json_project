from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jsonschema import validate, ValidationError
import json

app = FastAPI()

# Load schema
with open("ticket_schema.json") as f:
    schema = json.load(f)

class Ticket(BaseModel):
    ticketId: str
    priority: str
    createdAt: str

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    try:
        validate(instance=ticket.dict(), schema=schema)
        return {"message": "✅ Ticket validated successfully", "data": ticket.dict()}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"❌ Validation failed: {e.message}")