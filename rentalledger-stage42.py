# === Stage 42: Add CSV export without external dependencies ===
# Project: RentalLedger
def export_to_csv(records, filename):
    """Export a list-of-dicts ledger to CSV without external dependencies."""
    import csv
    if not records:
        return
    fieldnames = list(records[0].keys())
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in records:
            writer.writerow(row)
