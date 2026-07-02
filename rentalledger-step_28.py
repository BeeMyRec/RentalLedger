# === Stage 28: Add overdue item detection based on due dates ===
# Project: RentalLedger
from datetime import date, timedelta
from typing import List, Dict, Any

def detect_overdue_items(ledger_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Identify overdue maintenance tasks and rental payments."""
    today = date.today()
    overdue_list = []
    
    for entity_type in ['maintenance', 'payments']:
        if entity_type not in ledger_data:
            continue
            
        for item in ledger_data[entity_type]:
            due_date_str = item.get('due_date')
            status = item.get('status', '')
            
            if not due_date_str or status == 'completed':
                continue
                
            try:
                due_date = date.fromisoformat(due_date_str)
                
                # Consider overdue if past due date and not completed
                is_overdue = (today > due_date) and ('overdue' not in status.lower())
                
                if is_overdue:
                    item['is_overdue'] = True
                    days_late = (today - due_date).days
                    item['days_late'] = days_late
                    
                    # Flag critical items immediately overdue (>30 days)
                    if days_late > 30:
                        item['severity'] = 'critical'
                    else:
                        item['severity'] = 'warning'
                    
                    overdue_list.append(item)
            except ValueError:
                continue
                
    return overdue_list
