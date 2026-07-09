# === Stage 41: Add plain text import for a simple line-based format ===
# Project: RentalLedger
def load_lines(path):
    """Read a simple line-based text format and return a list of stripped non-empty lines."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = fh.read()
    except FileNotFoundError:
        return []
    if not data.strip():
        return []
    return [line for line in data.splitlines() if line.strip()]
