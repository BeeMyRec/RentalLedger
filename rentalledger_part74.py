# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: RentalLedger
def snapshot_diff(before, after):
    """Compare two states and return a human-readable diff summary."""
    if before == after:
        return "No changes detected."
    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        b_val = before.get(key)
        a_val = after.get(key)
        if isinstance(b_val, dict) and isinstance(a_val, dict):
            sub_diff = snapshot_diff(b_val, a_val)
            changes.append(f"{key}: {sub_diff}")
        elif b_val != a_val:
            changes.append(f"{key}: '{b_val}' -> '{a_val}'")
    return "\n".join(changes) if changes else "No changes detected."
