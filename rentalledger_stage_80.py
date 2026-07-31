# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: RentalLedger
def print_usage():
    """Display usage information."""
    print("RentalLedger - Rental Management System")
    print("\nUsage:")
    print("  python rental_ledger.py --help       Show this help message")
    print("  python rental_ledger.py              Start the interactive menu")
    print("\nFeatures:")
    print("  Properties: Add, view, and manage properties.")
    print("  Tenants: Register tenants and track their details.")
    print("  Payments: Record payments made by tenants.")
    print("  Maintenance: Log maintenance requests and repairs.")
    print("  Documents: Upload and store property documents.")

if __name__ == "__main__":
    print_usage()
