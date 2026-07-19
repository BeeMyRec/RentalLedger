# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: RentalLedger
def bulk_delete(self, record_type: str) -> int:
        """Delete multiple records of a given type when confirmed."""
        if self.confirmation_mode is False and record_type in (
            "property", "tenant", "payment", "maintenance"
        ):
            raise PermissionError(
                f"Bulk delete of {record_type} requires confirmation mode to be enabled."
            )

        table = getattr(self, record_type + "_table") if hasattr(self, record_type + "_table") else None
        if table is None:
            return 0

        count = len(table)
        table.clear()
        print(f"[Bulk Delete] Removed {count} {record_type}(s).")
        return count
