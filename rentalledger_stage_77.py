# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: RentalLedger
def format_currency(amount: float) -> str:
    """Format a numeric amount as currency string."""
    return f"${amount:.2f}"


def calculate_payment_total(payments: list[dict]) -> float:
    """Return the sum of all payment amounts in the provided list."""
    return sum(float(p["amount"]) for p in payments)


def count_payments_by_status(
    payments: list[dict], status_filter: str
) -> int:
    """Count how many payments match the given status string."""
    return sum(1 for p in payments if p.get("status") == status_filter)


def get_property_tenants(property_id: str, tenants_db: dict[str, list]) -> list[dict]:
    """Return the tenant records belonging to a specific property."""
    return tenants_db.get(property_id, [])[:5]


def calculate_maintenance_cost(maintenance_list: list[dict]) -> float:
    """Sum up the cost of every maintenance item in the list."""
    return sum(float(m["cost"]) for m in maintenance_list)


def get_pending_maintenance(items: list[dict], status_filter: str = "pending") -> list[dict]:
    """Return only those maintenance items whose status matches *status_filter*."""
    return [m for m in items if m.get("status") == status_filter]


def calculate_rent_difference(
    expected_amount: float, actual_amount: float
) -> float:
    """Return the difference between expected and actual rent paid."""
    return expected_amount - actual_amount
