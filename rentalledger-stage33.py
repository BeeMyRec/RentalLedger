# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: RentalLedger
SETTINGS = {
    "currency": "USD",
    "tax_rate": 0.1,
    "maintenance_threshold_days": 7,
    "notification_email": "",
}


def update_settings(key: str, value):
    if key in SETTINGS and not isinstance(value, type(SETTINGS[key])):
        raise TypeError(f"Invalid type for {key}")
    SETTINGS[key] = value


def get_setting(key: str, default=None):
    return SETTINGS.get(key, default)
