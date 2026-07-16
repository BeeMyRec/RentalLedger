# === Stage 53: Add command help text and usage examples ===
# Project: RentalLedger
HELP_TEXT = (
    "RentalLedger - A simple rental management tool.\n"
    "Usage examples:\n"
    "  python main.py --help\n"
    "  python main.py properties list\n"
    "  python main.py tenants add --name Alice --email alice@example.com\n"
    "  python main.py payments record --tenant Alice --amount 800 --date 2024-01-15\n"
    "  python main.py maintenance log --property 3B --issue leaky faucet\n"
    "  python main.py documents upload --doc lease.pdf --property 3B\n"
)
