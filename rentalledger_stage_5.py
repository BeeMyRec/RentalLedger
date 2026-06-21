# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: RentalLedger
def update_property(property_id, updates):
    if property_id not in properties:
        raise ValueError(f"Property {property_id} not found")
    for key, value in updates.items():
        if hasattr(properties[property_id], key):
            setattr(properties[property_id], key, value)
        else:
            raise AttributeError(f"Attribute {key} does not exist on Property object")

def update_tenant(tenant_id, updates):
    if tenant_id not in tenants:
        raise ValueError(f"Tenant {tenant_id} not found")
    for key, value in updates.items():
        if hasattr(tenants[tenant_id], key):
            setattr(tenants[tenant_id], key, value)
        else:
            raise AttributeError(f"Attribute {key} does not exist on Tenant object")

def update_payment(payment_id, updates):
    if payment_id not in payments:
        raise ValueError(f"Payment {payment_id} not found")
    for key, value in updates.items():
        if hasattr(payments[payment_id], key):
            setattr(payments[payment_id], key, value)
        else:
            raise AttributeError(f"Attribute {key} does not exist on Payment object")

def update_maintenance(maint_id, updates):
    if maint_id not in maintenance_requests:
        raise ValueError(f"Maintenance request {maint_id} not found")
    for key, value in updates.items():
        if hasattr(maintenance_requests[maint_id], key):
            setattr(maintenance_requests[maint_id], key, value)
        else:
            raise AttributeError(f"Attribute {key} does not exist on MaintenanceRequest object")

def update_document(doc_id, updates):
    if doc_id not in documents:
        raise ValueError(f"Document {doc_id} not found")
    for key, value in updates.items():
        if hasattr(documents[doc_id], key):
            setattr(documents[doc_id], key, value)
        else:
            raise AttributeError(f"Attribute {key} does not exist on Document object")
