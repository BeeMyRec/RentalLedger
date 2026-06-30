# === Stage 24: Add grouped summaries by category or status ===
# Project: RentalLedger
from collections import defaultdict

def generate_grouped_summary(ledger, group_by='category'):
    summary = defaultdict(lambda: {'total_amount': 0, 'count': 0})
    for item in ledger['transactions']:
        key = item.get(group_by) or 'Uncategorized'
        if isinstance(item.get('amount'), (int, float)):
            summary[key]['total_amount'] += item['amount']
            summary[key]['count'] += 1
    
    result = []
    for category, data in sorted(summary.items()):
        avg = round(data['total_amount'] / data['count'], 2) if data['count'] > 0 else 0.0
        result.append({
            'category': category,
            'total_amount': data['total_amount'],
            'average_amount': avg,
            'transaction_count': data['count']
        })
    return list(result)
