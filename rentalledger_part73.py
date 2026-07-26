# === Stage 73: Add a lightweight HTML report export ===
# Project: RentalLedger
import os, csv, datetime

def export_report(data_rows, output_path):
    if not data_rows:
        return False
    fieldnames = list(data_rows[0].keys())
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_rows)
    return os.path.exists(output_path) and os.path.getsize(output_path) > 0

def generate_summary_report(properties, tenants, payments):
    total_revenue = sum(p["amount"] for p in payments)
    occupied = len([t for t in tenants if any(t["property_id"] == p["id"] and t["status"] == "occupied" for p in properties)])
    return {"total_properties": len(properties), "occupied_units": occupied, "payments_count": len(payments), "total_revenue": total_revenue}

def export_summary(properties, tenants, payments):
    summary = generate_summary_report(properties, tenants, payments)
    report_path = os.path.join("reports", "summary.csv")
    return export_report([summary], report_path)
