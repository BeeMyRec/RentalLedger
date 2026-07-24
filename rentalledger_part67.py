# === Stage 67: Add a function that returns key project metrics ===
# Project: RentalLedger
def project_metrics(records, tenants):
    """Return compact summary metrics for the RentalLedger."""
    total_income = sum(r.get("amount", 0) for r in records if r.get("type") == "income")
    total_maintenance = sum(r.get("cost", 0) for r in records if r.get("type") == "maintenance")
    active_tenants = [t for t in tenants if any(t["name"] in r.get("tenant_name", "") or r.get("tenant_id", "") == str(id(t)) for r in records)]
    return {
        "total_income": total_income,
        "total_maintenance_cost": total_maintenance,
        "net_revenue": total_income - total_maintenance,
        "record_count": len(records),
        "tenant_count": len(set(r.get("tenant_name", "") for r in records)),
    }
