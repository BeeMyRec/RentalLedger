# === Stage 40: Add plain text report export ===
# Project: RentalLedger
def export_report(records, path="ledger_report.txt"):
    with open(path, "w") as f:
        for r in records:
            if r["type"] == "payment":
                f.write(f"Payment: ${r['amount']:.2f} from {r['tenant']} on {r['date']}\n")
            elif r["type"] == "maintenance":
                f.write(f"Maintenance: {r['cost']:.2f} for {r['property']} on {r['date']}\n")
            elif r["type"] == "document":
                f.write(f"Document uploaded: {r['name']} for property {r.get('property', 'N/A')}\n")
