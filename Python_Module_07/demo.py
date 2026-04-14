from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, creature_type) -> None:
        self.name = name
        self.type = creature_type
    
    @abstractmethod
    def attack(self) -> str:
        pass


class MyClass(Creature):

    def attack(self) -> str:
        return "this is a test"
    
object = MyClass("taha", "person")