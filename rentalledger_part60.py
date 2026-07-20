# === Stage 60: Add saved views for frequently used filters ===
# Project: RentalLedger
class SavedView:
    def __init__(self, name, filters=None, sort_by=None):
        self.name = name
        self.filters = filters or {}
        self.sort_by = sort_by

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {"name": self.name, "filters": self.filters, "sort_by": self.sort_by}


class SavedViewManager:
    def __init__(self, ledger=None):
        self._views = {}
        self.ledger = ledger

    def register_view(self, view):
        if not isinstance(view, SavedView):
            raise ValueError("Only SavedView instances are allowed")
        if view.name in self._views:
            raise KeyError(f"View '{view.name}' already exists")
        self._views[view.name] = view

    def get_view(self, name):
        return self._views.get(name)

    def apply_saved_view(self, name, context=None):
        if name not in self._views:
            raise KeyError(f"Saved view '{name}' does not exist")
        saved = self._views[name]
        filters = dict(saved.filters)
        for key, value in filters.items():
            if hasattr(context, key):
                setattr(context, key, value)
        return context

    def list_views(self):
        return [v.to_dict() for v in sorted(self._views.values(), key=lambda x: x.name)]


class PropertySavedView(SavedView):
    pass
