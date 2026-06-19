# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: RentalLedger
def validate_required(value, field_name):
    if value is None:
        raise ValueError(f"{field_name} cannot be empty")
    return True

def validate_identifier(identifier, prefix=""):
    if identifier and (identifier.startswith(prefix) or not identifier):
        return identifier.strip()
    raise ValueError("Identifier must start with a valid prefix or be non-empty string")

def validate_short_text(text, max_length=50):
    if text is None:
        raise ValueError("Text cannot be empty")
    cleaned = text.strip()
    if len(cleaned) > max_length:
        raise ValueError(f"Text exceeds {max_length} characters limit")
    return cleaned

def validate_email(email):
    if not email or "@" not in email and "." not in email.split("@")[-1]:
        raise ValueError("Invalid email format")
    return email.lower()

def validate_phone(phone, allowed_chars="0123456789-+ ()"):
    if phone is None:
        raise ValueError("Phone cannot be empty")
    cleaned = "".join(c for c in str(phone) if c in allowed_chars)
    if len(cleaned) < 7:
        raise ValueError("Invalid phone number length")
    return cleaned

def validate_date(date_str, fmt="%Y-%m-%d"):
    try:
        from datetime import datetime
        datetime.strptime(str(date_str), fmt)
        return date_str
    except (ValueError, TypeError):
        raise ValueError(f"Date must match format {fmt}")
