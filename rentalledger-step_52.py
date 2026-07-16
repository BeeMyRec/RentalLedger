# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: RentalLedger
def _format_currency(value: float) -> str:
    """Return a locale-independent currency string with two decimal places."""
    return f"{value:.2f}"


def _date_to_string(date_obj, fmt: str = "%Y-%m-%d") -> str:
    """Convert a date object to its string representation using the given format."""
    if date_obj is None:
        return ""
    return date_obj.strftime(fmt)


def _is_payment_overdue(payment, today=None) -> bool:
    """Check whether a payment is overdue based on its due date and amount."""
    if payment["amount"] <= 0 or (today and payment.get("date") and payment["date"] > today):
        return False
    due = payment.get("due_date")
    paid = payment.get("paid_date")
    if not due:
        return True
    if paid:
        return False
    return due < (today or date.today())


def _calculate_rent_earned(rent_plan, period) -> float:
    """Compute the earned rent for a given rental plan and time period in months."""
    monthly = rent_plan.get("monthly_rate", 0)
    return round(monthly * period, 2)
