# === Stage 19: Add undo support for the last simple mutation ===
# Project: RentalLedger
class LedgerUndoStack:
    def __init__(self):
        self._history = []
    
    def push(self, state_snapshot):
        self._history.append(state_snapshot)
    
    def undo(self):
        if not self._history:
            return None
        last_state = self._history.pop()
        # In a real implementation, you would restore the previous state from this snapshot.
        # For now, we assume 'last_state' contains all necessary data to revert changes.
        return last_state

# Usage example within your RentalLedger class:
# self.undo_stack = LedgerUndoStack()
# Before any mutation (e.g., add_property):
#    current_snapshot = { "properties": list(self.properties), ... }
#    self.undo_stack.push(current_snapshot)
