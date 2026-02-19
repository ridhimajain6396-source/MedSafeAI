import json

def load_medicines():
    with open("data/medicines.json", "r") as f:
        return json.load(f)

def load_interactions():
    with open("data/interactions.json", "r") as f:
        return json.load(f)
