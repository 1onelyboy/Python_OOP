def crisis_handle(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: File access failed")
        print("STATUS: Crisis handled, security maintained\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files_name = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for name in files_name:
        crisis_handle(name)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
