# === Stage 38: Add data integrity checks for broken references ===
# Project: RentalLedger
def check_integrity(db: dict) -> list[str]:
    """Validate that every payment, maintenance, and document reference a real property/tenant."""
    errors = []
    props = db.get("properties", [])
    tenants = db.get("tenants", [])
    payments = db.get("payments", [])
    maintenances = db.get("maintenances", [])
    documents = db.get("documents", [])

    prop_ids = {p["id"] for p in props} if isinstance(props, list) else set()
    tenant_ids = {t["id"] for t in tenants} if isinstance(tenants, list) else set()

    for pay in payments:
        pid = pay.get("property_id")
        tid = pay.get("tenant_id")
        if pid and pid not in prop_ids:
            errors.append(f"Payment #{pay['id']} references unknown property {pid}")
        if tid and tid not in tenant_ids:
            errors.append(f"Payment #{pay['id']} references unknown tenant {tid}")

    for mnt in maintenances:
        pid = mnt.get("property_id")
        tid = mnt.get("tenant_id")
        if pid and pid not in prop_ids:
            errors.append(f"Maintenance #{mnt['id']} references unknown property {pid}")
        if tid and tid not in tenant_ids:
            errors.append(f"Maintenance #{mnt['id']} references unknown tenant {tid}")

    for doc in documents:
        pid = doc.get("property_id")
        tid = doc.get("tenant_id")
        if pid and pid not in prop_ids:
            errors.append(f"Document #{doc['id']} references unknown property {pid}")
        if tid and tid not in tenant_ids:
            errors.append(f"Document #{doc['id']} references unknown tenant {tid}")

    return errors
