# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: RentalLedger
def format_currency(amount):
    return f"${amount:,.2f}"

def format_date(date_obj):
    if date_obj is None:
        return "-"
    try:
        from datetime import datetime
        return datetime.strftime(date_obj, "%Y-%m-%d")
    except Exception:
        return str(date_obj)

def print_table(headers, rows, max_width=60):
    if not headers or not rows:
        return
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = len(str(val))
            col_widths[i] = max(col_widths[i], min(w, max_width // len(headers)))
    header_line = " | ".join(str(h).ljust(col_widths[j]) for j, h in enumerate(headers))
    print(header_line)
    separator = "-+-".join("-" * w for w in col_widths)
    print(separator)
    for row in rows:
        line = " | ".join((str(v) if v is not None else "-").ljust(col_widths[j]) for j, v in enumerate(row))
        print(line)

def format_record(record):
    lines = []
    for key, val in record.items():
        display_val = format_currency(val) if isinstance(val, (int, float)) else format_date(val) if hasattr(val, 'strftime') else str(val)
        lines.append(f"{key}: {display_val}")
    return "\n".join(lines)
