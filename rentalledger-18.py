# === Stage 18: Add an activity log with timestamps and action names ===
# Project: RentalLedger
from datetime import datetime, timezone
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class ActivityLog:
    def __init__(self):
        self._entries: list[dict] = []

    def log(self, action_name: str, target_type: str, target_id: int | None = None) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_name,
            "target_type": target_type,
            "target_id": target_id,
        }
        self._entries.append(entry)

    def get_recent(self, limit: int = 10) -> list[dict]:
        return self._entries[-limit:] if len(self._entries) > limit else self._entries.copy()
