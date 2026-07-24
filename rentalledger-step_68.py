# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: RentalLedger
def generate_changelog(activity_log: list) -> str:
    """Generate a compact changelog from the activity log."""
    if not activity_log:
        return "No changes recorded."
    
    lines = []
    for entry in activity_log[-20:]:  # Last 20 entries
        date, action, detail = entry
        lines.append(f"{date} - {action}: {detail}")
    
    return "\n".join(lines)

# Example usage with a sample activity log
activity_log = [
    ("2024-01-01", "Added feature", "RentalLedger v68: Added compact changelog from activity log."),
    ("2024-01-01", "Fixed bug", "Resolved issue with property status updates."),
]

print(generate_changelog(activity_log))
