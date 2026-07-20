# === Stage 61: Add performance timing for core list and search operations ===
# Project: RentalLedger
import time

def benchmark_ledger(self):
    """Run timing tests on core list and search operations."""
    iterations = 1000 if len(self.properties) < 50 else 100
    for op_name, func in [("list_properties", self.list_properties),
                           ("search_tenant", lambda: next((t for t in self.tenants if t.name == "Test"), None))]:
        times = [time.perf_counter_ns() - time.perf_counter_ns() for _ in range(iterations)]
        print(f"[{op_name}] avg={sum(times)/len(times):.1f}ns, max={max(times)}ns")

    elapsed = {
        "list_properties": sum(self._timings.get("list_properties", [])[-iterations:]) / iterations * 1e-9 if self._timings.get("list_properties") else None,
        "search_tenant": sum(self._timings.get("search_tenant", [])[-iterations:]) / iterations * 1e-9 if self._timings.get("search_tenant") else None,
    }
    for k in elapsed:
        if elapsed[k] is not None:
            print(f"[{k}] avg={elapsed[k]:.4f}s")
