# === Stage 44: Add backup creation for the data file ===
# Project: RentalLedger
import os, shutil, time

def create_backup(data_path: str) -> str | None:
    """Create a timestamped backup of the data file and return its path."""
    if not os.path.isfile(data_path):
        print(f"[{time.strftime('%H:%M:%S')}] No source data file – skipping backup.")
        return None
    bak_dir = os.path.join(os.path.dirname(data_path), "backups")
    os.makedirs(bak_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    bak_name = f"{os.path.basename(data_path)}.backup_{ts}"
    bak_path = os.path.join(bak_dir, bak_name)
    shutil.copy2(data_path, bak_path)
    print(f"[{time.strftime('%H:%M:%S')}] Backup created: {bak_name}")
    return bak_path
