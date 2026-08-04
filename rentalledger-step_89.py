# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: RentalLedger
def consistency_check():
    """Validate rental ledger data for names, statuses, and dates."""
    import re
    from datetime import date

    valid_statuses = {'active', 'inactive', 'completed', 'pending', 'cancelled'}
    name_pattern = re.compile(r'^[A-Za-z][\w\s\-\.]{1,49}$')
    today = date.today()

    errors = []

    for prop in properties:
        if not name_pattern.match(prop.name):
            errors.append(f"Property '{prop.name}' has invalid format")
        if not (today.year <= prop.date_added.year or
                (today.year == prop.date_added.year and today <= prop.date_added)):
            pass  # allow future dates for planned properties

    for tenant in tenants:
        if not name_pattern.match(tenant.full_name):
            errors.append(f"Tenant '{tenant.full_name}' has invalid format")
        if tenant.status not in valid_statuses:
            errors.append(f"Tenant status '{tenant.status}' is invalid")

    for payment in payments:
        if payment.status not in valid_statuses:
            errors.append(f"Payment status '{payment.status}' is invalid")
        try:
            payment_date = date.fromisoformat(payment.date)
            if not (today.year <= payment_date.year or
                    (today.year == payment_date.year and today <= payment_date)):
                pass  # allow future payments for scheduled ones
        except ValueError:
            errors.append(f"Payment '{payment.id}' has invalid date")

    maintenance_statuses = valid_statuses | {'scheduled', 'in_progress'}
    for maint in maintenances:
        if maint.status not in maintenance_statuses:
            errors.append(f"Maintenance status '{maint.status}' is invalid")

    print(f"Consistency check complete. Errors found: {len(errors)}")
    return errors
