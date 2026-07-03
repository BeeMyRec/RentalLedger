# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: RentalLedger
from datetime import date, timedelta
from typing import List, Dict, Any

def get_upcoming_items(items: List[Dict[str, Any]], days_ahead: int = 7) -> List[Dict[str, Any]]:
    today = date.today()
    cutoff_date = today + timedelta(days=days_ahead)
    upcoming = []
    for item in items:
        due_date_str = item.get('due_date') or item.get('date', '')
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
            if today <= due_date <= cutoff_date and item.get('status') != 'completed':
                item['days_left'] = (due_date - today).days
                upcoming.append(item)
        except ValueError:
            continue
    return sorted(upcoming, key=lambda x: x.get('due_date', date.max))

def get_overdue_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    today = date.today()
    overdue = []
    for item in items:
        due_date_str = item.get('due_date') or item.get('date', '')
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
            if today > due_date and (item.get('status') != 'completed' or item.get('overdue_status')):
                overdue.append(item)
        except ValueError:
            continue
    return sorted(overdue, key=lambda x: x.get('due_date', date.min))
