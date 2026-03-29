class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        try:
            if not plant_name:
                raise PlantError
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError:
            print("Error adding plant: Plant name cannot be empty!")

    def water_plants(self, tank: bool) -> None:
        try:
            print("Opening watering system")
            if not self.plants:
                raise WaterError("No plants to water!")
            elif not tank:
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"{e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        try:
            if not plant_name:
                raise ValueError("Plant name cannot be empty!")
            if water_level > 10:
                raise ValueError(f"Water level {water_level}"
                                 " is too high (max 10)")
            elif water_level < 1:
                raise ValueError(f"Water level {water_level}"
                                 " is too low (min 1)")
            if sunlight_hours < 2:
                raise ValueError(f"Sunlight hours {sunlight_hours}"
                                 " is too low (min 2)")
            elif sunlight_hours > 12:
                raise ValueError(f"Sunlight hours {sunlight_hours}"
                                 " is too high (max 12)")
            else:
                print(f"{plant_name}: healthy (water: {water_level}, sun: "
                      f"{sunlight_hours})")
        except ValueError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    garden = GardenManager()
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant(None)

    print("\nWatering plants...")
    garden.water_plants(True)

    print("\nChecking plant health...")
    garden.check_plant_health("tomato", 5, 8)
    garden.check_plant_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
