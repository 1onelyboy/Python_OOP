class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        print(f"\n{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 156 // 100
        print(f"{self.name} provides {shade} square meters of shade")

    def display(self) -> None:
        print(f"\n{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutri_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutri_value = nutri_value

    def nutritional_value(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutri_value}")

    def display(self) -> None:
        print(f"\n{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.display()
    flower1.bloom()
    flower2 = Flower("Tulip", 30, 60, "yellow")
    flower2.display()
    flower2.bloom()
    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.display()
    tree1.produce_shade()
    tree2 = Tree("Balsam", 1500, 29220, 30)
    tree2.display()
    tree2.produce_shade()
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", "C")
    vegetable1.display()
    vegetable1.nutritional_value()
    vegetable2 = Vegetable("Carrot", 10, 75, "fall", "B")
    vegetable2.display()
    vegetable2.nutritional_value()
