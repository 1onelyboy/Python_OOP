class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
plants = [plant1, plant2, plant3]


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display()


if __name__ == "__main__":
    ft_garden_data()
