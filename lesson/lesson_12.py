from abc import ABC, abstractmethod


# ЧАСТЬ 1: Абстракция - Абстрактный класс Animal
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# ЧАСТЬ 2: Наследование - Классы Dog и Cat
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} говорит: Гав-гав!"


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} говорит: Мяу-Мяу!"


# ЧАСТЬ 3: Инкапсуляция - Класс Zoo (Зоопарк)
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals


# ЧАСТЬ 4: Полиморфизм - Работа с разными животными
def animal_sound(animal):
    print(animal.make_sound())


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# Нельзя создать объект Animal напрямую, так как он не знает,
# что за звук должен издавать животное в зоопарке
# В классе Animal мы указываем что для дочернего класса
# обязательно нужно исполнить метод make_sound, так как повесили на него
# декоратор и далее в дочернем классе уже пайтон обязательно проверит звук
