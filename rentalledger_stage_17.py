# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: RentalLedger
class DryRunContext:
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.changes = []

    def record(self, action, entity_id, details=None):
        if self.enabled:
            self.changes.append({"action": action, "entity_id": entity_id, **details})
        return True  # Always succeed in dry-run mode to mimic real behavior without side effects

    def get_summary(self):
        if not self.changes:
            return None
        return f"DRY-RUN MODE: {len(self.changes)} operations would be performed:\n" + "\n".join(
            f"- [{c['action']}] Entity {c['entity_id']}: {c.get('details', {})}" for c in self.changes
        )

    def clear(self):
        self.changes.clear()
