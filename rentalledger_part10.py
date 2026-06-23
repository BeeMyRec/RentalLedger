# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: RentalLedger
class SearchFilter:
    def __init__(self, data):
        self.data = list(data)  # Copy to avoid mutating original
        self._index = None
    
    def _build_index(self):
        if self._index is not None:
            return
        self._index = {}
        for item in self.data:
            key_fields = []
            if 'property_name' in item and item['property_name']:
                key_fields.append(item['property_name'].lower())
            if 'tenant_name' in item and item['tenant_name']:
                key_fields.append(item['tenant_name'].lower())
            if 'address' in item and item['address']:
                key_fields.append(item['address'].lower())
            if 'payment_amount' in item:
                try:
                    key_fields.append(str(float(item['payment_amount'])))
                except (ValueError, TypeError):
                    pass
            for field in key_fields:
                if field not in self._index:
                    self._index[field] = []
                self._index[field].append(item)

    def search(self, query):
        if not query or not self.data:
            return list(self.data)
        
        # Normalize query
        q = query.lower().strip()
        if not q:
            return list(self.data)
            
        # Check index first for speed
        if self._index is None:
            self._build_index()
        
        candidates = set()
        if q in self._index:
            candidates.update(self._index[q])
        
        # If no direct match, try fuzzy partial matches on key fields
        if not candidates and len(q) > 2:
            for item in self.data:
                combined_text = ""
                if 'property_name' in item: combined_text += " " + str(item['property_name'])
                if 'tenant_name' in item: combined_text += " " + str(item['tenant_name'])
                if 'address' in item: combined_text += " " + str(item['address'])
                
                # Simple substring check (case-insensitive)
                if q in combined_text.lower():
                    candidates.add(id(item))
        
        return [item for i, item in enumerate(self.data) if id(item) in candidates]

# Usage example:
# filter = SearchFilter(ledger_data)
# results = filter.search("apartment 4")
