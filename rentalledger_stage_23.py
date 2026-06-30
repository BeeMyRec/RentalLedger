# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: RentalLedger
class TagManager:
    def __init__(self, ledger):
        self._ledger = ledger
        self._tags = {}  # {tag_name: {"count": int, "items": [item_id]}}

    def add_tag(self, item_id, tag_name):
        if tag_name not in self._tags:
            self._tags[tag_name] = {"count": 0, "items": []}
        self._tags[tag_name]["count"] += 1
        self._tags[tag_name]["items"].append(item_id)

    def remove_tag(self, item_id, tag_name):
        if tag_name in self._tags and item_id in self._tags[tag_name]["items"]:
            self._tags[tag_name]["count"] -= 1
            self._tags[tag_name]["items"].remove(item_id)

    def get_summary(self, tag_name=None):
        if not tag_name:
            return {name: data["count"] for name, data in self._tags.items()}
        return {"total": self._tags.get(tag_name, {}).get("count", 0)}
