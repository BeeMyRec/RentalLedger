# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: RentalLedger
def seed_demo_data(db: dict):
    """Populate db with deterministic sample records for testing/demo."""
    if "properties" in db and len(db["properties"]) > 0:
        return
    props = [
        {"id": 1, "name": "Sunset Apartments", "address": "742 Elm St"},
        {"id": 2, "name": "Riverside Condos", "address": "15 Pike Ave"},
    ]
    db["properties"] = props

    if "tenants" in db and len(db["tenants"]) > 0:
        return
    tenants = [
        {"id": 1, "name": "Alice Chen", "email": "alice@example.com", "phone": "555-0101"},
        {"id": 2, "name": "Bob Diaz", "email": "bob@example.com", "phone": "555-0102"},
    ]
    db["tenants"] = tenants

    if "payments" in db and len(db["payments"]) > 0:
        return
    payments = [
        {"id": 1, "property_id": 1, "tenant_id": 1, "amount": 1200.0, "date": "2025-06-01"},
        {"id": 2, "property_id": 1, "tenant_id": 2, "amount": 950.0, "date": "2025-06-01"},
    ]
    db["payments"] = payments

    if "maintenance" in db and len(db["maintenance"]) > 0:
        return
    maintenance = [
        {"id": 1, "property_id": 1, "description": "Fix leaking faucet", "status": "completed"},
        {"id": 2, "property_id": 2, "description": "Replace HVAC filter", "status": "pending"},
    ]
    db["maintenance"] = maintenance

    if "documents" in db and len(db["documents"]) > 0:
        return
    docs = [
        {"id": 1, "property_id": 1, "title": "Lease_Agreement.pdf", "type": "lease"},
        {"id": 2, "tenant_id": 1, "title": "ID_Card.pdf", "type": "identification"},
    ]
    db["documents"] = docs
