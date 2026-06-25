# === Stage 14: Add file load support with fallback demo data ===
# Project: RentalLedger
import json, os, random
DATA_FILE = "ledger_data.json"
def load_or_seed():
    if not os.path.exists(DATA_FILE):
        demo = {
            "properties": [{"id": 1, "address": "123 Main St", "monthly_rent": 1500}],
            "tenants": [{"id": 1, "name": "Alice Smith", "property_id": 1}],
            "payments": [],
            "maintenance": []
        }
        with open(DATA_FILE, 'w') as f: json.dump(demo, f)
    else:
        try:
            with open(DATA_FILE, 'r') as f: return json.load(f)
        except Exception:
            with open(DATA_FILE, 'w') as f: json.dump(demo, f); return demo

def randomize_demo():
    if os.path.exists(DATA_FILE):
        data = load_or_seed()
        for p in data["properties"]:
            p["status"] = "occupied" if random.random() > 0.3 else "vacant"
        with open(DATA_FILE, 'w') as f: json.dump(data, f)
