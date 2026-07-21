# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: RentalLedger
def score_property(prop: dict) -> float:
    """Return a priority score for a property based on maintenance backlog and lease expiry."""
    score = 0.0
    if prop.get("maintenance_items") and len(prop["maintenance_items"]) > 3:
        score += 40.0
    elif prop.get("maintenance_items") and len(prop["maintenance_items"]) > 1:
        score += 20.0

    lease_end = prop.get("lease_expiry", "9999-12-31")
    try:
        days_left = (datetime.date.fromisoformat(lease_end) - datetime.date.today()).days
        if days_left < 60:
            score += 50.0
        elif days_left < 180:
            score += 25.0
    except Exception:
        pass

    return score
