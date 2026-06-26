# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: RentalLedger
class CommandDispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, command_name: str, handler_func):
        self._handlers[command_name.lower()] = handler_func

    def dispatch(self, raw_input: str) -> tuple[str, object]:
        cmd_parts = raw_input.strip().split(maxsplit=1)
        if not cmd_parts:
            return "error", "Empty command"
        cmd_name = cmd_parts[0]
        args_str = cmd_parts[1] if len(cmd_parts) > 1 else ""
        handler = self._handlers.get(cmd_name.lower())
        if not handler:
            return f"error", f"Unknown command: {cmd_name}"
        try:
            result = handler(args_str)
            return "ok", result
        except Exception as e:
            return "error", str(e)
