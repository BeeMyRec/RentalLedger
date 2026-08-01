# === Stage 83: Add regression tests for the final demo workflow ===
# Project: RentalLedger
import unittest


class TestDemoWorkflow(unittest.TestCase):
    """Regression test for the end-to-end demo workflow."""

    def setUp(self):
        from rentalledger.models import Property, Tenant, Payment, Maintenance, Document
        self.prop = Property(name="Apartment 101", address="123 Main St")
        self.tenant = Tenant(name="Alice Doe", email="alice@example.com")
        self.payment = Payment(amount=850.00, date="2024-06-01", tenant=self.tenant, property=self.prop)
        self.maintenance = Maintenance(description="Leaky faucet", status="open", property=self.prop)
        self.document = Document(name="lease.pdf", url="https://example.com/lease")

    def test_demo_workflow(self):
        """Simulate adding a tenant to a property, recording payments and maintenance."""
        from rentalledger.app import RentalLedgerApp
        app = RentalLedgerApp()
        app.add_property(self.prop)
        self.assertTrue(app.get_property("Apartment 101") is not None)
        app.add_tenant(self.tenant)
        app.add_payment(self.payment)
        app.add_maintenance(self.maintenance)
        app.add_document(self.document)

        ledger = app.get_ledger()
        self.assertEqual(ledger.properties["Apartment 101"].tenant_name, "Alice Doe")
        self.assertAlmostEqual(ledger.payments["2024-06-01"], 850.00, places=2)
        self.assertIn("Leaky faucet", ledger.maintenance_descriptions)


if __name__ == "__main__":
    unittest.main()
