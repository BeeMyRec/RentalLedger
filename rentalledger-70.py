# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: RentalLedger
import json, pathlib
from datetime import datetime

DATA_FILE = pathlib.Path(__file__).parent / "data.json"

def clear_state(ledger: dict) -> None:
    """Reset the ledger to a clean state."""
    if not ledger.get("_cleared", False):
        raise ValueError("Clearing is disabled for safety. Set 'cleared' flag first.")
    ledger.update({
        "properties": [],
        "tenants": [],
        "payments": [],
        "maintenance": [],
        "documents": [],
        "_cleared": True,
        "created_at": datetime.utcnow().isoformat(),
    })
