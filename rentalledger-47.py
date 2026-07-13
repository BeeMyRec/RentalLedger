# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: RentalLedger
if __name__ == "__main__":
    # --- Demo Scenario: End-to-end rental workflow for a single property ---
    from RentalLedger import Property, Tenant, Payment, MaintenanceRequest, DocumentStore

    prop = Property("Sunset Apartments", address="123 Ocean Drive")
    tenant = Tenant(name="Alice Johnson", email="alice@example.com")
    store  = DocumentStore()

    # 1. Register property and tenant; sign a lease document
    doc_lease = store.store(Document(
        title="Lease Agreement",
        content=f"Tenant: {tenant.name}\nProperty: {prop.name}\nAddress: {prop.address}",
        date=date.today(),
    ))
    prop.register(tenant, doc_id=doc_lease.id)

    # 2. Record monthly rent payment (due on the 1st)
    pmt = Payment(amount=1500.0, due_date=date(2026, 7, 1), status="paid")
    prop.payments.append(pmt)

    # 3. Log a maintenance request and track resolution
    req = MaintenanceRequest(description="Leaky faucet in unit A", severity=Severity.MEDIUM)
    prop.maintenance_requests.append(req)
    req.status = Status.RESOLVED
    store.store(Document(
        title="Maintenance Resolution – Leaky Faucet",
        content=f"Fixed on {date.today()}. Replaced washer.",
        date=date.today(),
    ))

    # 4. Print summary of the demo run
    print(f"{prop.name} — tenant: {tenant.name}")
    print(f"  Payments this month: ${pmt.amount:.2f} ({pmt.status})")
    print(f"  Maintenance items: {len(prop.maintenance_requests)} (last status={req.status.value})")
