# === Stage 22: Add favorite records and quick favorite listing ===
# Project: RentalLedger
class FavoriteManager:
    def __init__(self, ledger):
        self.ledger = ledger
        self._favorites = set()

    def toggle_favorite(self, record_id):
        if record_id in self._favorites:
            self._favorites.remove(record_id)
            return False
        else:
            self._favorites.add(record_id)
            return True

    def is_favorite(self, record_id):
        return record_id in self._favorites

    def get_favorites_summary(self):
        favorites = []
        for item_type, items in self.ledger.items():
            for idx, item in enumerate(items):
                if self.is_favorite(item['id']):
                    favorites.append({
                        'type': item_type,
                        'index': idx + 1,
                        'data': item
                    })
        return favorites

    def save_to_file(self, filename='favorites.json'):
        import json
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list(self._favorites), f)

    def load_from_file(self, filename='favorites.json'):
        try:
            import json
            with open(filename, 'r', encoding='utf-8') as f:
                self._favorites = set(json.load(f))
        except FileNotFoundError:
            pass
