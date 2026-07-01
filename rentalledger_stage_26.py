# === Stage 26: Add weekly summary calculations ===
# Project: RentalLedger
def calculate_weekly_summary(data):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    weekly_income = 0.0
    weekly_expenses = 0.0
    
    for record in data:
        if isinstance(record, dict):
            try:
                rec_date = date.fromisoformat(record['date'])
                if week_start <= rec_date < week_end:
                    amount = float(record.get('amount', 0))
                    category = record.get('category', 'other')
                    
                    if category in ('income', 'rent'):
                        weekly_income += amount
                    elif category in ('expense', 'maintenance', 'repair'):
                        weekly_expenses += amount
            except (KeyError, ValueError):
                continue
    
    return {
        "week_start": week_start.isoformat(),
        "week_end": week_end.isoformat(),
        "total_income": round(weekly_income, 2),
        "total_expenses": round(weekly_expenses, 2)
    }
