import json
from jsonschema import validate, ValidationError

with open("ticket_schema.json") as f:
    schema = json.load(f)

def test_valid_ticket():
    ticket = {"ticketId": "ABCD1234", "priority": "high", "createdAt": "2026-04-27T19:00:00Z"}
    validate(instance=ticket, schema=schema)

def test_invalid_ticket():
    ticket = {"ticketId": "123", "priority": "urgent", "createdAt": "not-a-date"}
    try:
        validate(instance=ticket, schema=schema)
        assert False, "Validation should fail"
    except ValidationError:
        assert True