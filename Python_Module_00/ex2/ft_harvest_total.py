def ft_harvest_total():
    sum = 0
    for i in range(3):
        day = int(input(f"Day {i + 1} harvest: "))
        sum += day

    print(f"Total harvest: {sum}")
