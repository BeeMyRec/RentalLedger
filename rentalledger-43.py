# === Stage 43: Add CSV import for the primary record type ===
# Project: RentalLedger
def import_properties_csv(filepath):
    """Import properties from a CSV with columns: id, name, address, city, state, zip_code."""
    import csv
    props = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            props.append(Property(
                id=row['id'],
                name=row['name'],
                address=row['address'],
                city=row.get('city', ''),
                state=row.get('state', ''),
                zip_code=row.get('zip_code', '')
            ))
    return props

def import_tenants_csv(filepath):
    """Import tenants from a CSV with columns: id, name, email, phone."""
    import csv
    tenants = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tenants.append(Tenant(
                id=row['id'],
                name=row['name'],
                email=row.get('email', ''),
                phone=row.get('phone', '')
            ))
    return tenants

def import_payments_csv(filepath):
    """Import payments from a CSV with columns: id, tenant_id, property_id, amount, date."""
    import csv
    payments = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            payments.append(Payment(
                id=row['id'],
                tenant_id=int(row['tenant_id']),
                property_id=int(row['property_id']),
                amount=float(row['amount']),
                date=row.get('date', '')
            ))
    return payments

def import_maintenance_csv(filepath):
    """Import maintenance records from a CSV with columns: id, description, cost, status."""
    import csv
    records = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(MaintenanceRecord(
                id=row['id'],
                description=row.get('description', ''),
                cost=float(row.get('cost', 0)),
                status=row.get('status', '')
            ))
    return records

def import_documents_csv(filepath):
    """Import documents from a CSV with columns: id, title, file_path, uploaded_by."""
    import csv
    docs = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            docs.append(Document(
                id=row['id'],
                title=row.get('title', ''),
                file_path=row.get('file_path', ''),
                uploaded_by=row.get('uploaded_by', '')
            ))
    return docs
