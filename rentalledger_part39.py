# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: RentalLedger
def repair_integrity(db_path: str) -> dict:
    """Run simple integrity checks and fix common data issues."""
    results = {"ok": 0, "fixed": 0, "errors": []}
    try:
        import sqlite3
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Check for orphaned payments (payments referencing non-existent tenants or properties)
        cursor.execute("""
            SELECT COUNT(*) FROM payments p 
            WHERE NOT EXISTS (SELECT 1 FROM tenants t WHERE t.id = p.tenant_id)
        """)
        orphan_payments = cursor.fetchone()[0]
        if orphan_payments > 0:
            print(f"Warning: {orphan_payments} payment(s) reference non-existent tenant(s).")
            cursor.execute("""UPDATE payments SET status = 'invalid' WHERE NOT EXISTS (SELECT 1 FROM tenants t WHERE t.id = p.tenant_id)""")
            conn.commit()
            results["fixed"] += orphan_payments

        # Check for orphaned maintenance records
        cursor.execute("""
            SELECT COUNT(*) FROM maintenance m 
            WHERE NOT EXISTS (SELECT 1 FROM properties pr WHERE pr.id = m.property_id)
        """)
        orphan_maintenance = cursor.fetchone()[0]
        if orphan_maintenance > 0:
            print(f"Warning: {orphan_maintenance} maintenance record(s) reference non-existent property(ies).")
            cursor.execute("""UPDATE maintenance SET status = 'invalid' WHERE NOT EXISTS (SELECT 1 FROM properties pr WHERE pr.id = m.property_id)""")
            conn.commit()
            results["fixed"] += orphan_maintenance

        # Check for duplicate property names with same address
        cursor.execute("""
            SELECT COUNT(*) FROM properties p 
            WHERE name IN (SELECT name FROM properties GROUP BY name HAVING COUNT(*) > 1)
                AND address IN (SELECT address FROM properties GROUP BY address HAVING COUNT(*) > 1)
        """)
        dup_properties = cursor.fetchone()[0]
        if dup_properties > 0:
            print(f"Warning: {dup_properties} property(ies) may have duplicate names and addresses.")

        # Validate date formats in maintenance records
        cursor.execute("""SELECT COUNT(*) FROM maintenance WHERE status_date IS NOT NULL""")
        bad_dates = cursor.fetchone()[0]
        if bad_dates > 0:
            print(f"Warning: {bad_dates} maintenance record(s) have non-NULL status dates but may be invalid.")

        conn.close()
        results["ok"] += 1
    except Exception as e:
        results["errors"].append(str(e))
    return results
