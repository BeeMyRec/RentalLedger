# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: RentalLedger
class SortableLedger:
    def __init__(self, ledger):
        self._ledger = ledger
        self._sort_key_map = {
            'title': lambda x: (x.get('property', {}).get('name') or '', x['id']),
            'date': lambda x: (x['created_at'], x['id']),
            'priority': lambda x: (-int(x.get('priority', 0)), x['id']),
            'updated': lambda x: (-float(x.get('updated_at', 0) or ''), x['id'])
        }

    def sort(self, by='title'):
        key_func = self._sort_key_map.get(by.lower(), self._sort_key_map['date'])
        return sorted(self._ledger.items(), key=key_func)
