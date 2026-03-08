class Plant:
    def __init__(self, name: str, height: int, lifetime: int) -> None:
        self.name = name
        self.height = height
        self.lifetime = lifetime
        self.initial_height = height

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.lifetime += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.lifetime} days old")

    def get_growth(self):
        return self.height - self.initial_height


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Cactus", 20, 35)
plants = [plant1, plant2]


def ft_plant_growth() -> None:
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    print("=== Day 7 ===")
    for day in range(6):
        for plant in plants:
            plant.grow()
            plant.age()
    for plant in plants:
        plant.get_info()
        print(f"Growth this week: +{plant.get_growth()}cm")


if __name__ == "__main__":
    ft_plant_growth()
