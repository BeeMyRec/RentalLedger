# === Stage 58: Add bulk update behavior for selected records ===
# Project: RentalLedger
def bulk_update(self, table_name: str, records: list[dict]) -> int:
        """Update multiple rows in one table using a single SQL statement."""
        if not records or not self._table_exists(table_name):
            return 0
        placeholders = ", ".join(["%s"] * len(records))
        columns = ", ".join(self._get_columns(table_name))
        sql = f"UPDATE {self.db} SET {columns} = VALUES({placeholders}) WHERE id IN ({', '.join(['?'] * len(records))});"
        args = []
        for rec in records:
            row = [rec.get(col, None) for col in self._get_columns(table_name)]
            row[0] = rec["id"]  # keep id as the primary key
            args.extend(row)
        try:
            with self.db.transaction() as cur:
                cur.execute(sql, args)
            return cur.rowcount
        except Exception:
            return 0
