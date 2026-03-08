class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> int:
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"

    def get_score(self) -> int:
        return self.height


class FloweringPlant(Plant):
    BLOOM_BONUS: int = 20

    def __init__(self, name: str, height: int, color: str,
                 status: str = "blooming") -> None:
        super().__init__(name, height)
        self.color: str = color
        self.status: str = status

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} " \
               f"flowers ({self.status})"

    def get_type(self) -> str:
        return "flowering"

    def get_score(self) -> int:
        return self.height + self.BLOOM_BONUS


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_points}"

    def get_type(self) -> str:
        return "prize"

    def get_score(self) -> int:
        return self.height + self.BLOOM_BONUS


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        @staticmethod
        def count_by_type(garden: "GardenManager") -> list[int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                plant_type = plant.get_type()
                if plant_type == "regular":
                    regular += 1
                elif plant_type == "flowering":
                    flowering += 1
                elif plant_type == "prize":
                    prize += 1
            return [regular, flowering, prize]

        @staticmethod
        def calculate_score(garden: "GardenManager") -> int:
            total: int = 0
            for plant in garden.plants:
                total += plant.get_score()
            return total

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.plant_count: int = 0
        self.total_growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, show_message: bool = True) -> None:
        self.plants.append(plant)
        self.plant_count += 1
        if show_message:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.total_growth += plant.grow()

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        r, f, p = GardenManager.GardenStats.count_by_type(self)
        print(f"\nPlants added: {self.plant_count}, Total growth: "
              f"{self.total_growth}cm")
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers\n")

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        return cls("New Owner")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    bob.add_plant(Plant("Bamboo", 50), show_message=False)
    bob.add_plant(FloweringPlant("Tulip", 22, "pink"), show_message=False)

    alice.grow_all()
    alice.report()

    print(f"Height validation test: {alice.validate_height(50)}")

    alice_score = GardenManager.GardenStats.calculate_score(alice)
    bob_score = GardenManager.GardenStats.calculate_score(bob)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
