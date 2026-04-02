def main() -> None:
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")

    try:
        file = open(file_name, "r")
        content = file.read()
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except (FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
