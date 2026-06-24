# === Stage 11: Add JSON export for the current application state ===
# Project: RentalLedger
def export_state_to_json(app):
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "properties": app.properties,
        "tenants": app.tenants,
        "payments": app.payments,
        "maintenance": app.maintenance,
        "documents": app.documents
    }
    with open("ledger_state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f"State exported to ledger_state.json ({len(app.properties)} properties)")
