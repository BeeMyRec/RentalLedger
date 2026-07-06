# === Stage 35: Add active user switching and user-specific records ===
# Project: RentalLedger
import sqlite3, json
from datetime import date, timedelta

def setup_user_switching(db_path="ledger.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Create users table for switching between active user contexts
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'tenant',  -- tenant or owner
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # Create user_activity table to track last active timestamp per user
    c.execute('''CREATE TABLE IF NOT EXISTS user_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id),
        activity_date DATE DEFAULT CURRENT_DATE,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )''')

    # Create a helper table for storing user-specific notes/preferences
    c.execute('''CREATE TABLE IF NOT EXISTS user_preferences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id),
        setting_key TEXT UNIQUE NOT NULL,
        setting_value TEXT DEFAULT '',
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )''')

    conn.commit()
    return conn
