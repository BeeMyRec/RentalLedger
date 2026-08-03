# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: RentalLedger
def reports_equal(report_a, report_b):
    """Return True if two exported reports contain identical records."""
    return sorted(report_a) == sorted(report_b)


def diff_keys(report_a, report_b):
    """Show which record keys are unique to each report."""
    keys_a = set(report_a)
    keys_b = set(report_b)
    only_in_a = keys_a - keys_b
    only_in_b = keys_b - keys_a
    return {"only_in_first": sorted(only_in_a), "only_in_second": sorted(only_in_b)}


def summary_by_status(reports_list):
    """Aggregate counts per status across a list of reports."""
    from collections import Counter
    merged = []
    for r in reports_list:
        merged.extend(r)
    counts = Counter(item.get("status") or "unknown" for item in merged if isinstance(item, dict))
    return dict(sorted(counts.items()))


def compact_report(report):
    """Collapse a report into one-line rows for quick diff display."""
    out = []
    for i, rec in enumerate(report):
        if isinstance(rec, dict):
            parts = [f"{k}={v}" for k, v in sorted(rec.items())]
            out.append(" | ".join(parts))
        else:
            out.append(str(rec))
    return "\n".join(out)


def report_to_csv(report):
    """Convert a list of dicts to a simple CSV string."""
    if not report:
        return ""
    headers = sorted(report[0].keys())
    lines = [",".join(headers)]
    for row in report:
        lines.append(",".join(str(row.get(h, "")) for h in headers))
    return "\n".join(lines)


def find_mismatched_reports(reports_list):
    """Return indices of reports that differ from the first one."""
    base = sorted(reports_list[0]) if isinstance(reports_list[0], list) else list(reports_list[0])
    mismatched = []
    for idx, r in enumerate(reports_list):
        target = sorted(r) if isinstance(r, list) else list(r)
        if target != base:
            mismatched.append(idx)
    return mismatched


def total_revenue_by_period(reports_list):
    """Sum numeric 'amount' values per period key across reports."""
    totals = {}
    for r in reports_list:
        if isinstance(r, list):
            entries = r
        else:
            entries = [r]
        for item in entries:
            if not isinstance(item, dict):
                continue
            amount = item.get("amount") or 0
            period = item.get("period") or "unknown"
            totals[period] = totals.get(period, 0) + float(amount)
    return {"total": sum(totals.values()), "by_period": totals}


def quick_check(reports_list):
    """One-line boolean: all reports in the list are identical."""
    if not reports_list or len(set(id(r) for r in reports_list)) != 1:
        return False
    return reports_equal(*reports_list)
