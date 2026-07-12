# === Stage 46: Add a schema version field and migration helper ===
# Project: RentalLedger
SCHEMA_VERSION = 4

def migrate_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ledger'").fetchone():
        cur.execute(f"ALTER TABLE ledger ADD COLUMN schema_version INTEGER DEFAULT {SCHEMA_VERSION}")
        print(f"Migrated to schema version {SCHEMA_VERSION}")
    else:
        raise RuntimeError("Ledger table does not exist")
