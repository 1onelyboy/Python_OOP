from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:

    print("Testing factory")
    print(factory.create_base().describe())
    print(factory.create_base().attack())
    print(factory.create_evolved().describe())
    print(factory.create_evolved().attack())


def battle(factory1, factory2) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("\nTesting battle")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    test_factory(FlameFactory())
    print()
    test_factory(AquaFactory())

    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()