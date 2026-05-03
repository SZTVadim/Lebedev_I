# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виногдад")
print(fruits)

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
fruits_delete = fruits.pop()
print(fruits)
print(fruits_delete)

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
index = (fruits.index("банан"))
count_fruits = (fruits.count("банан"))
print(count_fruits)

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# ЗАДАНИЕ 5:
generators = [n ** 3 for n in range(1, 8)]
print(generators)
print(min(generators))
print(max(generators))

# ЗАДАНИЕ 6:
numbers1 = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
generators1 = [n for n in numbers if n > 10]
print(generators1)
print(sum(generators1))

# Задание 7:
city = ["москва", "санкт-петербург", "казань"]
city_big = [city.capitalize() for city in city]
print(city_big)
