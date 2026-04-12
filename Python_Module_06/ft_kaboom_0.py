import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")

    spell_name = "Fantasy"
    ingredients = "Earth, wind and fire"

    result = alchemy.grimoire.light_spell_record(spell_name, ingredients)
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
