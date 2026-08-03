# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: RentalLedger
# Sample CLI command transcripts for RentalLedger — Main Workflows
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from rental_ledger_cli import run_app

SAMPLE_TRANSCRIPTS = [
    {"prompt": "list properties",  "expected_output_lines": ["Property ID: P-001", "Address: 123 Oak St"]},
    {"prompt": "add property --id P-002 --address 456 Maple Ave --city Springfield --state IL", "expected_output_lines": ["Property added successfully.", "ID: P-002"]},
    {"prompt": "list tenants",       "expected_output_lines": ["Tenant ID: T-001", "Name: Alice Johnson"]},
    {"prompt": "add tenant --name Bob Smith --email bob@example.com --phone 555-0198", "expected_output_lines": ["Tenant added successfully.", "ID: T-002"]},
    {"prompt": "link tenant P-001 --tenant T-001",                        "expected_output_lines": ["Tenant linked to property P-001."]},
    {"prompt": "record payment --property P-001 --amount 1500.00 --date 2024-06-01 --description Rent June", "expected_output_lines": ["Payment recorded.", "Amount: $1500.00"]},
    {"prompt": "record payment --property P-001 --amount 300.00 --date 2024-06-05 --category maintenance --description AC repair", "expected_output_lines": ["Payment recorded.", "Category: Maintenance"]},
    {"prompt": "show property summary P-001",                        "expected_output_lines": ["Total Payments: $1800.00", "Maintenance Cost: $300.00"]},
]

for i, entry in enumerate(SAMPLE_TRANSCRIPTS):
    print(f"--- Transcript {i+1}: '{entry['prompt']}' ---")
    for line in entry["expected_output_lines"]:
        print(line)
