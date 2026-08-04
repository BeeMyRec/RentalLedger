# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: RentalLedger
def safer_get(record, key, default=None):
    """Return record[key] if present and non-empty else default."""
    try:
        v = record.get(key)
        return v if v is None or isinstance(v, bool) else (v if str(v).strip() else default)
    except Exception:
        return default

def safer_int(value, default=0):
    """Parse int safely; fall back to default."""
    try:
        s = str(value).strip()
        if not s or s.lower() == 'nan':
            return default
        return int(float(s))  # handles '3.0' -> 3
    except (ValueError, TypeError):
        return default

def safer_float(value, default=0.0):
    """Parse float safely; fall back to default."""
    try:
        s = str(value).strip()
        if not s or s.lower() == 'nan':
            return default
        return float(s)
    except (ValueError, TypeError):
        return default

def safer_bool(value, default=False):
    """Coerce to bool safely; fall back to default."""
    try:
        v = str(value).strip().lower() if value is not None else ''
        if not v or v == 'nan':
            return default
        return v in ('true', '1', 'yes')
    except Exception:
        return default

def safer_date(value, fmt='%Y-%m-%d'):
    """Parse common date formats; fall back to None."""
    if value is None or not str(value).strip():
        return None
    for f in [fmt, '%m/%d/%Y', '%d-%m-%Y', '%Y/%m/%d']:
        try:
            return datetime.strptime(str(value).strip(), f)
        except ValueError:
            continue
    return None
