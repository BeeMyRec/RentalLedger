# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: RentalLedger
import json, os, random, string, datetime


def _seed():
    return {
        "properties": [
            {"id": 1, "address": "123 Oak St", "type": "apartment", "num_units": 4},
            {"id": 2, "address": "456 Pine Ave", "type": "house", "num_units": 1},
        ],
        "tenants": [
            {"id": 10, "name": "Alice Johnson", "email": "alice@example.com"},
            {"id": 11, "name": "Bob Smith", "email": "bob@example.com"},
            {"id": 12, "name": "Charlie Davis", "email": "charlie@example.com"},
        ],
        "payments": [
            {"id": 100, "tenant_id": 10, "property_id": 1, "amount": 850, "date": "2026-07-01", "status": "paid"},
            {"id": 101, "tenant_id": 11, "property_id": 2, "amount": 1200, "date": "2026-07-05", "status": "pending"},
        ],
        "maintenance": [
            {"id": 200, "property_id": 1, "description": "Replace roof shingles", "cost": 3500, "date": "2026-07-10", "status": "open"},
            {"id": 201, "property_id": 2, "description": "Fix leaky faucet", "cost": 150, "date": "2026-07-12", "status": "in_progress"},
        ],
    }


def _generate_random():
    return {
        "name": f"Tenant {random.randint(100,999)}",
        "email": f"{string.ascii_lowercase}@example.com",
        "property_id": random.choice([1, 2]),
        "amount": round(random.uniform(500, 3000), 2),
        "date": datetime.date.today().isoformat(),
        "status": random.choice(["paid", "pending"]),
    }


def reset_demo_data(db_path: str = "data/ledger_db.json") -> dict:
    """Reset the ledger database to a clean demo state for manual testing."""
    seed_state = _seed()
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))
    with open(db_path, "w") as f:
        json.dump(seed_state, f, indent=2)
    print("Demo data reset complete.", flush=True)
    return seed_state


if __name__ == "__main__":
    reset_demo_data()
