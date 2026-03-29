def check_temperature(s: str) -> None | int:
    flag = 0
    try:
        temp = int(s)
        flag = 1
        if temp >= 0 and temp <= 40:
            print(f"Testing temperature: {s}")
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        print(f"Testing temperature: {s}")
        if flag == 1:
            print(f"Error: {e}\n")
        else:
            print(f"Error: '{s}' is not a valid number\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
