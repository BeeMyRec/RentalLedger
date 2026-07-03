# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: RentalLedger
def parse_date(date_str: str, formats=None) -> datetime.date | None:
    if formats is None:
        formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d.%m.%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: {', '.join(formats)}")
