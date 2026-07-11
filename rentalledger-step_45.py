# === Stage 45: Add restore from backup with validation ===
# Project: RentalLedger
def restore_ledger(backup_path, target_dir):
    """Restore a backup ledger and validate it before overwriting."""
    import os, json, datetime
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    with open(backup_path) as f:
        data = json.load(f)
    required_keys = {"properties", "tenants", "payments", "maintenance"}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Backup missing keys: {missing}")
    for key in ("properties", "tenants"):
        if not isinstance(data[key], list):
            raise ValueError(f"{key} must be a list")
    today = datetime.date.today().isoformat()
    if data.get("last_backup_date") != today:
        print(f"Warning: backup date {data.get('last_backup_date')} differs from today ({today})")
    for d in ["properties", "tenants", "payments", "maintenance"]:
        for item in data[d]:
            for field in ("id",):
                if field not in item and d == "properties":
                    raise ValueError(f"Property {item.get('name')} missing 'id'")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "ledger.json"), "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
