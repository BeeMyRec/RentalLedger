# === Stage 13: Add file save support using a configurable path ===
# Project: RentalLedger
import os, json, sys
from pathlib import Path
def get_config_path(): return (Path.home() / ".rental_ledger" / "config.json").resolve() if sys.platform != 'win32' else Path(os.environ.get('APPDATA', '')) / '.rental_ledger' / 'config.json'
def save_state(data: dict) -> None:
    try:
        cfg_path = get_config_path()
        cfg_path.parent.mkdir(parents=True, exist_ok=True)
        with open(cfg_path, 'w') as f: json.dump({'storage': str(cfg_path)}, f, indent=2)
    except Exception as e: print(f"Failed to save config: {e}")

def load_state() -> dict:
    try:
        cfg_path = get_config_path()
        if not cfg_path.exists(): return {'storage': None}
        with open(cfg_path) as f: data = json.load(f)
        storage_path = Path(data.get('storage'))
        if storage_path and storage_path.exists():
            with open(storage_path, 'r') as f: return {**data, '_db': json.load(f)}
    except Exception as e: print(f"Failed to load state: {e}")
    return {'storage': None}

def init_db(db_name='ledger.db'):
    import sqlite3
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS properties (id INTEGER PRIMARY KEY, name TEXT UNIQUE, address TEXT, rent REAL, status TEXT DEFAULT 'active')''')
    c.execute('''CREATE TABLE IF NOT EXISTS tenants (id INTEGER PRIMARY KEY, property_id INTEGER, name TEXT, email TEXT, FOREIGN KEY(property_id) REFERENCES properties(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY, tenant_id INTEGER, amount REAL, date TEXT, status TEXT DEFAULT 'pending', FOREIGN KEY(tenant_id) REFERENCES tenants(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS maintenance (id INTEGER PRIMARY KEY, property_id INTEGER, description TEXT, cost REAL, status TEXT DEFAULT 'open', FOREIGN KEY(property_id) REFERENCES properties(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, name TEXT, file_path TEXT, upload_date TEXT)''')
    conn.commit()
    return conn

def get_db_connection():
    state = load_state()
    if not state.get('_db'):
        db_file = Path(state['storage']).parent / 'data' / 'ledger.db' if state['storage'] else 'ledger.db'
        save_state({'_db': str(db_file)})
        return init_db(str(db_file))
    return state['_db'].get('conn', None)
