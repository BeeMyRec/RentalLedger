# === Stage 31: Add compact table rendering for long lists ===
# Project: RentalLedger
def render_compact_table(data, columns=None):
    if not data: return ""
    if columns is None: columns = list(data[0].keys())
    header = " | ".join(columns)
    separator = "-+-".join(["-" * len(c) for c in columns])
    lines = [header, separator]
    for row in data[:20]:  # Limit to first 20 rows for compactness
        line = " | ".join(str(row.get(col, "")) for col in columns)
        lines.append(line)
    if len(data) > 20:
        lines[-1] += f" ... (+{len(data)-20} more)"
    return "\n".join(lines)
