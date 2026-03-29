class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error(name: str) -> None:
    try:
        raise PlantError(f"The {name} plant is wilting!")
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")


def test_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Testing WaterError...")
        print(f"Caught WaterError: {e}\n")


def test_all_garden_errors() -> None:
    print("Testing catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error("tomato")
    test_water_error()
    test_all_garden_errors()
    print("\nAll custom error types work correctly!")
