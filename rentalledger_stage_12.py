# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: RentalLedger
def load_json_safe(path: str) -> dict | None:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except json.JSONDecodeError as e:
        error_msg = f"Malformed JSON in {path}: {e}"
        if hasattr(e, 'msg'):
            error_msg += f"\n  Details: {e.msg} at line {e.lineno}, column {e.colno}"
        print(error_msg)
        return None
