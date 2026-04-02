def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read())
    except FileNotFoundError:
        print("ERROR: Classified data file not found!")

    try:
        with open("security_protocols.txt", "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    except Exception as e:
        print(f"ERROR during preservation: {e}")

    print("\nAll vault operations completed with maximum security.")

if __name__ == "__main__":
    main()
