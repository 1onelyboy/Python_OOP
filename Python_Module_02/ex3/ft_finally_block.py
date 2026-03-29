class NoneError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    flag = 0
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                flag = 1
                raise NoneError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except NoneError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")
        if flag == 0:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    plants = ["tomato", "lettuce", "carrots"]
    plants1 = ["tomato", None, "carrots"]

    print("Testing normal watering...")
    water_plants(plants)

    print("\nTesting with error...")
    water_plants(plants1)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
