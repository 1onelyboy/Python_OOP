def garden_operations(error_type: str) -> None:
    if error_type == "ValueError":
        try:
            int("abc")
        except ValueError:
            print("Testing ValueError...")
            print("Caught ValueError: invalid literal for int()\n")
    elif error_type == "ZeroDivisionError":
        try:
            1 / 0
        except ZeroDivisionError:
            print("Testing ZeroDivisionError...")
            print("Caught ZeroDivisionError: division by zero\n")
    elif error_type == "FileNotFoundError":
        try:
            file = open("missing.txt")
            file.close
        except FileNotFoundError:
            print("Testing FileNotFoundError...")
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    elif error_type == "KeyError":
        try:
            plant_info = {
                'name': 'rose',
                'height': 30,
                'age': 25,
            }
            print(plant_info['missing_plant'])
        except KeyError:
            print("Testing KeyError...")
            print("Caught KeyError: 'missing\\_plant'\n")
    elif error_type == "multiple errors together":
        try:
            int("abc")
            1 / 0
            file = open("missing.txt")
            file.close
            dic = {'key': 'value'}
            print(dic['key1'])
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Testing multiple errors together...")
            print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations("ValueError")
    garden_operations("ZeroDivisionError")
    garden_operations("FileNotFoundError")
    garden_operations("KeyError")
    garden_operations("multiple errors together")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
