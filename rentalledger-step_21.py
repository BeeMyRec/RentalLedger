# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: RentalLedger
from datetime import date, timedelta
import shutil
import os
ARCHIVE_DIR = "archive"
def archive_records(records, cutoff_date=None):
    if not records: return
    if cutoff_date is None: cutoff_date = date.today() - timedelta(days=365)
    old = [r for r in records if (getattr(r, 'completed', False) or getattr(r, 'date', cutoff_date)) < cutoff_date]
    new = [r for r in records if r not in old]
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(os.path.join(ARCHIVE_DIR, "ledger.dat"), "w") as f:
        for r in new: f.write(f"{type(r).__name__}\n{r.__dict__}\n")

def restore_records(source_file):
    if not os.path.exists(source_file): return []
    restored = []
    with open(source_file, "r") as f:
        content = f.read()
    for block in content.strip().split("\n\n"):
        lines = block.split("\n")
        if len(lines) < 2: continue
        cls_name = lines[0]
        data_lines = [l for l in lines[1:] if l.strip()]
        try:
            d = {}
            for line in data_lines:
                key, val = line.split("=", 1)
                d[key.strip()] = eval(val.strip())
            restored.append(eval(cls_name)(**d))
        except Exception: continue
    return restored
