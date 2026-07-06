# === Stage 36: Add templates for quickly creating common records ===
# Project: RentalLedger
class RecordTemplate:
    """Templates for quickly creating common ledger records."""

    @staticmethod
    def new_property(name, address, rent_amount):
        return Property(name=name, address=address, rent_amount=rent_amount)

    @staticmethod
    def new_tenant(property_obj, first_name, last_name):
        return Tenant(first_name=first_name, last_name=last_name, property=property_obj)

    @staticmethod
    def new_payment(tenant, amount, date_str=None):
        if date_str is None:
            import datetime as _dt
            date_str = _dt.date.today().isoformat()
        return Payment(amount=amount, date=date_str, tenant=tenant)

    @staticmethod
    def new_maintenance(property_obj, description, cost, start_date=None):
        if start_date is None:
            import datetime as _dt
            start_date = _dt.date.today().isoformat()
        return Maintenance(description=description, cost=cost, start_date=start_date, property=property_obj)

    @staticmethod
    def new_document(title, file_path, category="general"):
        return Document(title=title, file_path=file_path, category=category)
