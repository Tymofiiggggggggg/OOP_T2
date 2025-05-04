from abc import ABC, abstractmethod

# 1. Наслідування (Inheritance)
# Створюємо абстрактний базовий клас
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        # Абстрактний метод — має бути реалізований у підкласах
        pass

    def describe(self):
        # Метод з реалізацією
        print(f"This is a {self.__class__.__name__} named {self.name}")

# 2. Інкапсуляція (Encapsulation)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  # Приватний атрибут

    def make_sound(self):
        print("Woof!")

    # Методи доступу до приватного атрибуту
    def get_breed(self):
        return self.__breed

    def set_breed(self, new_breed):
        self.__breed = new_breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color  # Приватний атрибут

    def make_sound(self):
        print("Meow!")

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

# 3. Поліморфізм (Polymorphism)
# Створюємо колекцію об'єктів різних підкласів
zoo = [
    Dog("Rex", "Labrador"),
    Cat("Murka", "White")
]

# Викликаємо абстрактний метод через базовий інтерфейс
for animal in zoo:
    animal.describe()
    animal.make_sound()
