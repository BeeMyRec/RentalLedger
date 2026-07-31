# === Stage 81: Add final README text as a module string with usage examples ===
# Project: RentalLedger
def usage_example():
    """Demonstrate a minimal RentalLedger workflow end-to-end."""
    from rental_ledger import Property, Tenant, Payment, Maintenance, Document

    # Create a property and assign it to a tenant
    prop = Property(name="123 Oak St", address="Springfield, IL 62704")
    tenant = Tenant(name="Alice Johnson", email="alice@example.com")
    prop.assign(tenant)

    # Record monthly rent payment
    payment = Payment(amount=850.0, date="2024-01-01", description="January rent")
    prop.record_payment(payment)

    # Log a maintenance request
    maint = Maintenance(description="Leaky faucet in kitchen", status="open", priority="medium")
    prop.log_maintenance(maint)

    # Attach a document (e.g., lease agreement)
    doc = Document(name="lease_agreement.pdf", content=b"--- Lease content ---")
    prop.attach_document(doc)

    # Print summary for verification
    print(f"Property: {prop.name}")
    print(f"Tenant: {tenant.name} -> paid ${payment.amount:.2f}")
    print(f"Maintenance: [{maint.status}] {maint.description}")
    print(f"Documents attached: {len(prop.documents)}")

if __name__ == "__main__":
    usage_example()
