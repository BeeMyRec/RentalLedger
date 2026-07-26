# === Stage 72: Add Markdown report export ===
# Project: RentalLedger
def export_markdown_report(self):
    """Export ledger to a compact Markdown report."""
    lines = ["# Rental Ledger Report\n"]
    for p in self.properties:
        lines.append(f"## Property: {p.name}\n")
        lines.append(f"- Address: {p.address}\n- Monthly Rent: ${p.monthly_rent:.2f}\n")
        for t in p.tenants:
            lines.append(f"### Tenant: {t.name} (Unit {t.unit_number})\n")
            lines.append(f"- Email: {t.email}\n")
            if t.deposit_amount:
                lines.append(f"- Deposit Paid: ${t.deposit_amount:.2f}\n")
        for m in p.maintenance_log:
            lines.append(f"### Maintenance\n- Date: {m.date}, Issue: {m.issue}, Cost: ${m.cost:.2f}\n")
    return "\n".join(lines)
