# === Stage 25: Add daily summary calculations ===
# Project: RentalLedger
def calculate_daily_summary(data):
    """Compute daily financial summary for rental ledger."""
    if not data:
        return {}
    
    today = datetime.date.today()
    summaries = defaultdict(lambda: {
        'income': 0, 
        'expenses': 0, 
        'maintenance_count': 0, 
        'tenant_count': set(), 
        'property_ids': set()
    })
    
    for record in data['payments']:
        if record.get('date') == today:
            summaries[today]['income'] += record.get('amount', 0)
            summaries[today]['tenant_count'].add(record.get('tenant_id'))
            summaries[today]['property_ids'].add(record.get('property_id'))
            
    for expense in data['expenses']:
        if expense.get('date') == today:
            summaries[today]['expenses'] += expense.get('amount', 0)
            
    for maintenance in data['maintenance']:
        if maintenance.get('created_date') == today:
            summaries[today]['expenses'] += maintenance.get('estimated_cost', 0)
            summaries[today]['maintenance_count'] += 1
            
    return {date_str: dict(vals) for date_str, vals in summaries.items()}
