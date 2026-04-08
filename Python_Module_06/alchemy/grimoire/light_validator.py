from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    if ingredients in light_spell_allowed_ingredients():
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"