def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    words = ingredients.lower().split()
    for word in words:
        if word in light_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
