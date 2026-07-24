# === Stage 66: Add export of a short status dashboard ===
# Project: RentalLedger
def export_status_dashboard(properties, tenants, payments, maintenance):
    """Export a compact status dashboard from rental ledger data."""
    total_revenue = sum(p.amount for p in payments)
    active_tenants = len(tenants)
    avg_rent = (total_revenue / len(tenants)) if tenants else 0
    pending_maintenance = sum(1 for m in maintenance if not m.completed)
    dashboard = {
        "total_properties": len(properties),
        "active_tenants": active_tenants,
        "total_revenue": total_revenue,
        "avg_rent": round(avg_rent, 2),
        "pending_maintenance": pending_maintenance
    }
    return dashboard
