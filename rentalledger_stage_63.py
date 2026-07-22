# === Stage 63: Add relationships between records where useful ===
# Project: RentalLedger
# Step 63: Relationships between records where useful.
# Attach a property to its most recent maintenance ticket, store the tenant who made each payment, and link documents to their owner record.

def attach_relationships(db):
    """Update every Payment with its paying Tenant and every MaintenanceTicket with its Property."""
    for row in db["payments"]:
        pid = row[0]
        tid = row[2]  # tenant_id column
        if tid is not None:
            for trow in db["tenants"]:
                if trow[0] == tid:
                    row[3] = trow[1]  # store tenant name on Payment
                    break

    for row in db["maintenance_tickets"]:
        pid = row[2]  # property_id column
        if pid is not None:
            for prow in db["properties"]:
                if prow[0] == pid:
                    row[3] = prow[1]  # store property name on MaintenanceTicket
                    break

    for row in db["documents"]:
        rid = row[2]  # record_id column
        if rid is not None:
            for rname, rtable in [
                ("property", "properties"),
                ("tenant", "tenants"),
                ("payment", "payments"),
                ("maintenance_ticket", "maintenance_tickets"),
            ]:
                if rid == db[rtable][0]:
                    row[3] = rname  # store owner label on Document
                    break

    return db
