class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plants_data = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120],
        ]
    plants_number = 0
    for x in plants_data:
        plant = Plant(x[0], x[1], x[2])
        plant.display()
        plants_number += 1
    print(f"\nTotal plants created: {plants_number}")


if __name__ == "__main__":
    ft_plant_factory()
