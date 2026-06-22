# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: RentalLedger
class FilterMixin:
    def filter_by_status(self, statuses):
        return [item for item in self.items if getattr(item, 'status', None) in statuses]

    def filter_by_category(self, categories):
        return [item for item in self.items if getattr(item, 'category', None) in categories]

    def filter_by_owner(self, owners):
        return [item for item in self.items if getattr(item, 'owner_id', None) in owners]

    def filter_by_tag(self, tags):
        filtered = list(self.items)
        if not tags:
            return filtered
        tag_set = set(tags)
        result = []
        for item in filtered:
            item_tags = getattr(item, 'tags', [])
            if any(tag in tag_set for tag in item_tags):
                result.append(item)
        return result

    def apply_filters(self, statuses=None, categories=None, owners=None, tags=None):
        items = self.items
        if statuses:
            items = self.filter_by_status(statuses)
        if categories:
            items = self.filter_by_category(categories)
        if owners:
            items = self.filter_by_owner(owners)
        if tags:
            items = self.filter_by_tag(tags)
        return items
