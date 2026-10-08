import time
import sys
import random


def simulated_loading_task():
    # 10 minutes total = 600 seconds
    total_seconds = 600

    # Realistic operational log messages to print during execution
    messages = [
        "Synchronizing local repositories...",
        "Validating package integrity hashes...",
        "Allocating memory buffers...",
        "Optimizing data indexing clusters...",
        "Cleaning legacy compilation artifacts...",
        "Rebuilding system dependency trees...",
        "Verifying network handshake protocols..."
    ]

    print("Initializing deployment pipeline...")
    time.sleep(2)

    # Main progress bar loop running for 600 iterations (1 second each)
    for i in range(1, total_seconds + 1):
        time.sleep(1)

        # Calculate percentage and progress bar visual blocks
        percent = (i / total_seconds) * 100
        bar_length = 40
        filled_length = int(bar_length * i // total_seconds)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        # Periodically inject a technical log message to make it look authentic
        if i % 85 == 0 and i < total_seconds:
            log_msg = random.choice(messages)
            # Clear line first to prevent trailing artifact overlaps
            sys.stdout.write(f"\r\033[K[LOG] {log_msg}\n")

        # Print the updating progress line smoothly without creating new lines
        sys.stdout.write(f"\rProgress: |{bar}| {percent:.2f}% Complete ({i}/{total_seconds}s)")
        sys.stdout.flush()

    # Move cursor to a new line when the progress bar hits 100%
    print("\n")

    # 50/50 randomized ending sequence
    is_successful = random.choice([True, False])

    if is_successful:
        print("=" * 50)
        print("STATUS: SUCCESS")
        print("All operations completed successfully. Pipeline clean.")
        print("=" * 50)
    else:
        print("=" * 50)
        print("STATUS: FAILED")
        print("FATAL ERROR: Operation timed out. Connection reset by remote host.")
        print("=" * 50)


if __name__ == "__main__":
    try:
        simulated_loading_task()
    except KeyboardInterrupt:
        print("\n\nExecution aborted by user.")
