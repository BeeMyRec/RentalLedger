# === Stage 55: Add a setting to disable colorized output ===
# Project: RentalLedger
import os

# Disable colorized output if the environment variable is set to "1"
if os.environ.get("RENTAL_LEDGER_NO_COLOR") == "1":
    import sys
    from colorama import Fore, Style, deinit as _deinit
    try:
        # If we are already inside a block that uses Fore/Style, this is fine.
        # Otherwise, the terminal will just use plain text.
        pass  # Colorama fallback handled below if needed
    except Exception:
        pass

# Ensure colorama is initialized with no colors when disable flag is set
if os.environ.get("RENTAL_LEDGER_NO_COLOR") == "1":
    try:
        from colorama import init, Fore, Style, deinit as _deinit
        # Force colorama to use a non-colorful mode by monkey-patching
        original_init = init
        def no_color_init(*args, **kwargs):
            pass  # do nothing – we will override print functions below

        init.__wrapped__ = lambda *a, **kw: None  # dummy for inspection

        import colorama.main as _main
        # Re-initialize with our "no-color" behavior
        original_init(*args, **kwargs) if args else original_init()
    except Exception:
        pass

# If we are using a custom module that prints colored strings (e.g., RentalLedgerCLI),
# patch its print-like helpers to strip ANSI codes when the flag is set.
if os.environ.get("RENTAL_LEDGER_NO_COLOR") == "1":
    import re

    ansi_escape = re.compile(r"\x1B\[[0-9;]*m")

    def _strip_ansi(text):
        return ansi_escape.sub("", text) if isinstance(text, str) else text

    # Patch common print helpers if they exist in the project namespace
    for attr_name in ("print_report", "print_row", "report_to_terminal"):
        try:
            from RentalLedgerCLI import RentalLedgerCLI as cli_mod
            fn = getattr(cli_mod, attr_name)
            if callable(fn):
                setattr(cli_mod, attr_name, lambda *a, **kw: _strip_ansi(
                    fn(*a, **kw)))
        except (ImportError, AttributeError):
            pass

    # Also patch the top-level RentalLedgerCLI module's own print function
    try:
        from RentalLedgerCLI import print as cli_print
        import RentalLedgerCLI
        if callable(cli_print):
            def _cli_print(*args, **kwargs):
                text = " ".join(str(a) for a in args)
                return _strip_ansi(text)

            setattr(RentalLedgerCLI, "_original_print", cli_print.__wrapped__ or cli_print)
            setattr(RentalLedgerCLI, "print", _cli_print)
    except (ImportError, AttributeError):
        pass
