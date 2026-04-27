# Customer_support_json_project

## Features
- JSON Schema validation for customer support tickets
- FastAPI endpoint with Swagger UI
- CI/CD pipeline (lint + test) using GitHub Actions

## Files
- `ticket_schema.json` → JSON Schema definition
- `main.py` → FastAPI app with validation endpoint
- `requirements.txt` → Dependencies
- `.github/workflows/ci.yml` → CI/CD pipeline

## Visit Swagger UI
- http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload

## Example Requests
# Valid payload:

json
{
  "ticketId": "ABCD1234",
  "priority": "high",
  "createdAt": "2026-04-27T19:00:00Z"
}
# Invalid payload:

json
{
  "ticketId": "123",
  "priority": "urgent",
  "createdAt": "not-a-date"
}

## Testing
Run unit tests:

bash
pytest
CI/CD
The GitHub Actions workflow runs automatically on every push:

Black → code formatting check

Pytest → unit tests




