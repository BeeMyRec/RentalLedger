# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: RentalLedger
import os


def _is_duplicate_import(filepath, line):
    """Check if an import already exists in the file."""
    with open(filepath, 'r') as f:
        for existing_line in f:
            stripped = existing_line.strip()
            if stripped.startswith('import ') and stripped == line:
                return True
            elif stripped.startswith('from ') and 'import' in stripped:
                # Compare module and imported names
                parts = stripped.split('import')
                if len(parts) >= 2:
                    new_names = [n.strip() for n in parts[1].split(',')]
                    existing_parts = existing_line.split('import')
                    if len(existing_parts) >= 2:
                        existing_names = [n.strip() for n in existing_parts[1].split(',')]
                        # Check if all new names exist in existing imports
                        if all(name in existing_names for name in new_names):
                            return True
    return False


def _merge_imports(filepath, lines_to_add):
    """Add lines to the file only if they are not duplicates."""
    with open(filepath, 'a') as f:
        for line in lines_to_add:
            stripped = line.strip()
            # Skip empty lines or comments at start of new block
            if stripped == '' or stripped.startswith('#'):
                continue
            if _is_duplicate_import(filepath, line):
                print(f"Skipped duplicate import: {line}")
            else:
                f.write(line + '\n')


# Example usage:
if __name__ == "__main__":
    target_file = "RentalLedger.py"  # Adjust to your actual file path
    new_imports = [
        "import math",
        "from datetime import timedelta",
        "import json",
    ]

    _merge_imports(target_file, new_imports)
