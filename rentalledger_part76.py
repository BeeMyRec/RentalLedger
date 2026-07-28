# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: RentalLedger
import sys, signal

def main():
    def handle_sigint(signum, frame):
        print("\nRentalLedger interrupted by user.", flush=True)
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_sigint)
    if __name__ == "__main__":
        main()
