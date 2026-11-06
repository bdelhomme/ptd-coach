"""Validate the finite JSON Schema vocabulary used by the candidate contracts.

This is intentionally not a general-purpose JSON Schema implementation. Unknown
vocabulary fails closed so a future contract change needs an explicit migration.
"""

import json
from pathlib import Path


CONTRACTS = Path(__file__).resolve().parents[1] / "contracts/json-schemas"
KEYWORDS = {"$schema", "$id", "title", "description", "type", "enum", "required",
            "properties", "additionalProperties", "items"}
TYPES = {"object": dict, "array": list, "string": str, "boolean": bool,
         "null": type(None)}


def validate(value, schema):
    if set(schema) - KEYWORDS:
        raise ValueError("Unsupported contract vocabulary")
    kinds = schema.get("type", [])
    kinds = [kinds] if isinstance(kinds, str) else kinds
    if any(kind not in TYPES for kind in kinds):
        raise ValueError("Unsupported contract type")
    if kinds and not any(type(value) is TYPES[kind] for kind in kinds):
        raise ValueError("Invalid contract type")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError("Invalid contract enumeration")
    if isinstance(value, dict):
        if set(schema.get("required", [])) - set(value):
            raise ValueError("Missing contract fields")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False and set(value) - set(properties):
            raise ValueError("Unexpected contract fields")
        for key in set(value) & set(properties):
            validate(value[key], properties[key])
    if isinstance(value, list) and "items" in schema:
        for item in value:
            validate(item, schema["items"])


def validate_coach(value, kind):
    if kind not in {"request", "response"}:
        raise ValueError("Unknown contract")
    schema = json.loads((CONTRACTS / ("coach-" + kind + ".schema.json")).read_text())
    validate(value, schema)
