# === Stage 27: Add monthly summary calculations ===
# Project: RentalLedger
def calculate_monthly_summary(transactions, properties):
    from collections import defaultdict
    summary = defaultdict(lambda: {"income": 0, "expenses": 0})
    for t in transactions:
        if isinstance(t.get("amount"), (int, float)):
            key = f"{t['property_id']}-{t['month']}".lower()
            summary[key]["income"] += t["amount"] * (1 if t.get("type") == "rent" else -1)
            summary[key]["expenses"] += t["amount"] * (-1 if t.get("type") in ("maintenance", "repair") else 0)
    for prop_id, props in properties.items():
        name = props.get("name", "")
        print(f"{prop_id}: {name}")
        for key, data in sorted(summary.items()):
            if key.startswith(str(prop_id)):
                net = data["income"] - data["expenses"]
                print(f"  {key}: Income={data['income']}, Expenses={data['expenses']}, Net={net:.2f}")
