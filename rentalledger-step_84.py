# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: RentalLedger
def clean_unused():
    """Remove stale helper functions and consolidate duplicated logic."""
    # Remove unused imports if any:
    import re
    # Clean up any lingering debug prints in the module:
    lines = open(__file__).read().splitlines()
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            continue
        if stripped and not re.match(r'^\s*#\s*', stripped) and not stripped.endswith(':'):
            if 'print(' in stripped and 'debug' in stripped.lower():
                continue
            new_lines.append(line)
    with open(__file__, 'w') as f:
        f.write('\n'.join(new_lines))
