import elements as root_elements
from alchemy import elements


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{elements.create_earth()}' and '{elements.create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{root_elements.create_fire()}' and '{root_elements.create_water()}'"
    )
