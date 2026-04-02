import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print()
    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()

