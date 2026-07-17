# === Stage 56: Add compact error classes for domain failures ===
# Project: RentalLedger
class LedgerError(Exception):
    """Base for all domain errors."""

class PropertyNotExists(LedgerError):
    pass

class TenantAlreadyExist(LedgerError):
    pass

class PaymentFailed(LedgerError):
    pass

class MaintenanceOverdue(LedgerError):
    pass

class DocumentCorrupt(LedgerError):
    pass

class InvalidPeriod(LedgerError):
    pass
