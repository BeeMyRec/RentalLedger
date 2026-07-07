# === Stage 37: Add recommendations for the next useful action ===
# Project: RentalLedger
def get_dashboard_stats(self):
    """Return a compact summary dictionary for quick overview."""
    stats = {
        "properties": len(Property),
        "tenants": len(Tenant),
        "payments": len(Payment),
        "maintenance_issues": len(MaintenanceIssue),
        "documents": len(Document),
    }
    total_revenue = sum(p.amount for p in Payment if p.status == "completed")
    stats["total_revenue"] = total_revenue
    return stats

def get_due_payments(self):
    """Return a list of payments that are overdue or pending."""
    today = datetime.date.today()
    due = [p for p in Payment if p.status != "completed" and (today - p.due_date).days > 0]
    return sorted(due, key=lambda x: x.due_date)

def get_maintenance_summary(self):
    """Return maintenance issues grouped by status."""
    summary = {"open": [], "in_progress": [], "resolved": []}
    for issue in MaintenanceIssue:
        summary[issue.status].append(issue)
    return summary
