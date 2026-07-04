# === Stage 32: Add pagination helpers for long console output ===
# Project: RentalLedger
def paginate_output(lines, page_size=15):
    total_pages = (len(lines) + page_size - 1) // page_size if lines else 0
    for i in range(total_pages):
        start = i * page_size
        end = min(start + page_size, len(lines))
        print(f"--- Page {i+1}/{total_pages} ---")
        for line in lines[start:end]:
            print(line)
        if i < total_pages - 1:
            input("Press Enter to continue...")

def format_table(headers, rows):
    col_widths = [max(len(str(h)), max((len(str(r)) for r in row), default=0)) + 2 for h, row in zip(headers, zip(*rows))]
    header_line = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)
    data_lines = [" | ".join(str(r).ljust(w) for r, w in zip(row, col_widths)) for row in rows]
    return [header_line, separator] + data_lines

def print_summary(stats):
    if not stats:
        print("No summary available.")
        return
    lines = format_table(["Metric", "Value"], [[k, str(v)] for k, v in stats.items()])
    for line in lines:
        print(line)
