# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: RentalLedger
def colorize(text, color):
    colors = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m',
        'white': '\033[97m', 'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def print_ledger(self):
    for p in self.properties:
        print(f"\n{colorize(p.name, 'cyan')}")
        for t in p.tenants:
            print(f"  {colorize(t.name, 'green')} - {t.email}")
        for pay in p.payments:
            print(f"    Payment: ${pay.amount} ({pay.date})")
        for maint in p.maintenance:
            print(f"    Maintenance: {maint.description} - due {maint.due_date}")
