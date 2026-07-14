# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: RentalLedger
import unittest


class TestValidation(unittest.TestCase):
    def test_empty_tenant_name(self):
        self.assertFalse(Tenant.is_valid({"name": "", "email": "a@b.com"}))

    def test_invalid_email(self):
        self.assertFalse(Tenant.is_valid({"name": "A", "email": "not-an-email"}))


class TestCreation(unittest.TestCase):
    def test_create_tenant(self):
        tenant = Tenant.create(name="Alice", email="alice@example.com")
        self.assertEqual(tenant.name, "Alice")
        self.assertTrue(Tenant.is_valid(tenant.__dict__))

    def test_invalid_email_rejected(self):
        with self.assertRaises(Exception):
            Tenant.create(name="Bob", email="invalid")
