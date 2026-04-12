
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

import alchemy.grimoire.dark_spellbook # noqa : E402
ingredients = "Earth, wind and fire"
r = alchemy.grimoire.dark_spellbook.dark_spell_record("Fantasy", ingredients)
print(f"Testing record light spell: {r}")
