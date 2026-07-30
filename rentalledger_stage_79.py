# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: RentalLedger
import sys
sys.path.insert(0, '.')
from rental_ledger import Property, Tenant, Payment, Maintenance, Document, RentalLedgerApp, db


def _demo():
    app = RentalLedgerApp(db)
    # Create a property
    prop = Property("123 Oak Ave", "Apartment 4B", "Residential")
    app.db.insert(prop)

    # Add a tenant
    tenant = Tenant("John Doe", "john@example.com", "+1-555-0101")
    app.db.insert(tenant)

    # Create a lease and assign tenant to property
    lease = prop.create_lease(24, 1800.0, [tenant])
    app.db.insert(lease)

    # Record payments
    for i in range(6):
        pay = Payment("Monthly Rent", 1800.0, "Completed")
        lease.add_payment(pay)
        app.db.insert(pay)

    # Add maintenance request
    maint = Maintenance("Fix leaky faucet", "High")
    app.db.insert(maint)

    # Upload documents
    doc = Document("lease_agreement.pdf", 1024, "https://example.com/lease.pdf")
    app.db.insert(doc)

    print("=" * 50)
    print(f"Property: {prop.address} ({prop.unit})")
    print(f"Tenant:   {tenant.name}")
    print(f"Lease:    {len(lease.payments)} payments, total ${sum(p.amount for p in lease.payments):,.2f}")
    print(f"Maintenance: {maint.description} [{maint.priority}]")
    print(f"Documents:  {doc.file_name}")
    print("=" * 50)

_demo()
