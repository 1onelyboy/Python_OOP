def main() -> None:
    file_name = "new_discovery.txt"
    data = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    ]
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print(f"Initializing new storage unit: {file_name}")

        file = open(file_name, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        for line in data:
            file.write(line)
            print(line, end="")

        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

        file.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
