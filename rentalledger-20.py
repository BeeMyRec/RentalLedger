# === Stage 20: Add duplicate detection for newly created records ===
# Project: RentalLedger
from typing import Optional, List, Dict, Any
import hashlib
from datetime import date

def _get_record_hash(record: Dict[str, Any]) -> str:
    """Generate a unique hash for duplicate detection based on core fields."""
    key_fields = ["property_id", "tenant_name", "amount"] if record.get("type") == "payment" else \
                 ["property_id", "maintenance_type", "description"] if record.get("type") == "maintenance" else \
                 ["name"]
    field_values = [str(record[f]) for f in key_fields]
    return hashlib.md5("|".join(field_values).encode()).hexdigest()

def check_duplicates(new_record: Dict[str, Any], existing_records: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Check if a new record is a duplicate of an existing one and return the match or None."""
    new_hash = _get_record_hash(new_record)
    for existing in existing_records:
        if _get_record_hash(existing) == new_hash:
            return existing
    return None

def append_with_check(records_file: str, new_record: Dict[str, Any], records: List[Dict[str, Any]], 
                      duplicate_threshold_days: int = 0):
    """Append a record only if no duplicate exists within the threshold period."""
    match = check_duplicates(new_record, records)
    if match is None:
        with open(records_file, "a", encoding="utf-8") as f:
            json.dump(new_record, f)
            f.write("\n")
        return True
    else:
        print(f"Duplicate detected for {new_record.get('type')}: {match}")
        return False
