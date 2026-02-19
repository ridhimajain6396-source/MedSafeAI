from rapidfuzz import process
from modules.medicine_db import load_medicines

med_db = load_medicines()
medicine_names = [m["name"] for m in med_db]

def find_medicine(user_input):
    result = process.extractOne(user_input, medicine_names, score_cutoff=60)
    if result:
        match_name = result[0]
        for m in med_db:
            if m["name"] == match_name:
                return m
    return None
