def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))

    def f(day: int):
        if day > days_until_harvest:
            print("Harvest time!")
            return
        else:
            print(f"Day {day}")
            f(day + 1)
    f(1)
