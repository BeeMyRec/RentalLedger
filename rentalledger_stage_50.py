# === Stage 50: Add unit tests for import and export behavior ===
# Project: RentalLedger
import unittest
from rental_ledger import Ledger, Property, Tenant


class TestLedger(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger()

    def test_import_export_roundtrip(self):
        prop = Property("123 Main St", 200)
        tenant = Tenant("Alice Smith", "alice@example.com")
        self.ledger.add_property(prop)
        self.ledger.add_tenant(tenant)
        payload = self.ledger.export()
        new_ledger = Ledger()
        new_ledger.import_data(payload)
        self.assertEqual(len(new_ledger.properties), 1)
        self.assertEqual(len(new_ledger.tenants), 1)

    def test_import_empty(self):
        ledger = Ledger()
        payload = {"properties": [], "tenants": []}
        new_ledger = Ledger()
        new_ledger.import_data(payload)
        self.assertEqual(len(new_ledger.properties), 0)
        self.assertEqual(len(new_ledger.tenants), 0)


if __name__ == "__main__":
    unittest.main()
