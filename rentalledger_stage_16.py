# === Stage 16: Add argparse support for the most common commands ===
# Project: RentalLedger
import argparse

def main():
    parser = argparse.ArgumentParser(description="RentalLedger CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List properties
    list_parser = subparsers.add_parser('list-props', help='List all properties')
    list_props_args = list_parser.add_argument_group()
    
    # Add tenant to property
    add_tenant_parser = subparsers.add_parser('add-tenant', help='Add a new tenant')
    add_tenant_parser.add_argument('--prop-id', required=True, type=int, help='Property ID')
    add_tenant_parser.add_argument('--name', required=True, help='Tenant name')
    
    # Add payment
    pay_parser = subparsers.add_parser('add-payment', help='Record a new payment')
    pay_parser.add_argument('--prop-id', required=True, type=int, help='Property ID')
    pay_parser.add_argument('--amount', required=True, type=float, help='Payment amount')
    
    # Add maintenance request
    maint_parser = subparsers.add_parser('add-maintenance', help='Log a new maintenance issue')
    maint_parser.add_argument('--prop-id', required=True, type=int, help='Property ID')
    maint_parser.add_argument('--issue', required=True, help='Issue description')
    
    # View documents for property
    docs_parser = subparsers.add_parser('list-docs', help='List documents for a property')
    docs_parser.add_argument('--prop-id', required=True, type=int, help='Property ID')
    
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    
    # Placeholder logic to be implemented in main script
    print(f"Command executed: {args.command}")
    if hasattr(args, 'prop_id'):
        print(f"Target Property ID: {args.prop_id}")
    if hasattr(args, 'amount'):
        print(f"Amount: {args.amount}")

if __name__ == "__main__":
    main()
