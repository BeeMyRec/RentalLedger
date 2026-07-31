# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: RentalLedger
def demo():
    ledger = RentalLedger()
    prop = Property("123 Oak St", "Apartment A")
    tenant = Tenant("Alice Smith", "alice@example.com", "0987654321")
    ledger.add_property(prop)
    ledger.add_tenant(tenant)

    payment = Payment(
        tenant=tenant, amount=1200.0, date="2024-11-01", description="November rent"
    )
    ledger.process_payment(payment)

    maintenance = MaintenanceRequest(description="Leaky faucet", severity="medium")
    ledger.add_maintenance_request(maintenance)

    doc = Document("lease.pdf", "Signed lease for 123 Oak St")
    ledger.upload_document(doc)

    print(ledger.get_summary())
