# === Stage 57: Add structured result objects for command handlers ===
# Project: RentalLedger
class RentalLedgerResult:
    """Structured result objects returned by command handlers."""

    def __init__(self, success=True, message="", data=None, error=None):
        self.success = success
        self.message = message
        self.data = data
        self.error = error

    @staticmethod
    def ok(message="Operation successful", data=None):
        return RentalLedgerResult(success=True, message=message, data=data)

    @staticmethod
    def fail(error_message, exception=None):
        return RentalLedgerResult(success=False, message=error_message, error=str(exception) if exception else None)
