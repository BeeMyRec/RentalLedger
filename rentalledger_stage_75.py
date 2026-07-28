# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: RentalLedger
class ValidationReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def validate(self, ledger):
        if not ledger.properties:
            self.errors.append("No properties recorded.")
        else:
            for p in ledger.properties:
                if not p.address:
                    self.warnings.append(f"Property '{p.name}' has no address.")

        if not ledger.tenants:
            self.errors.append("No tenants recorded.")
        else:
            for t in ledger.tenants:
                if not t.name or not t.email:
                    self.errors.append(f"Tenant record is incomplete (name/email missing).")

        if not ledger.payments:
            self.errors.append("No payments recorded.")
        else:
            total = sum(p.amount for p in ledger.payments)
            if total <= 0:
                self.warnings.append("Total payment amount equals zero or negative.")

        if not ledger.maintenance:
            self.warnings.append("No maintenance records found; consider adding them.")

    def report(self):
        lines = ["=== RentalLedger Validation Report ==="]
        if self.errors:
            lines.append(f"\nErrors ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  ✗ {e}")
        if self.warnings:
            lines.append(f"\nWarnings ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  ⚠ {w}")
        if not self.errors and not self.warnings:
            lines.append("\n✓ All checks passed.")
        return "\n".join(lines)
