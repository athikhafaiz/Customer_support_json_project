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

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
