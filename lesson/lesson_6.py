# ЗАДАНИЕ 1: Работа со словарями и перебор элементов
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2,
    "город": "Москва"
}
print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)

for value in student.values():
    print(value)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}
del prices["груша"]
price = prices.pop("виноград")
print(prices)
print(price)
sale_prices = {key: value * 0.9 for key, value in prices.items()}
print(sale_prices)

# ЗАДАНИЕ 3: Объединение словарей
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}
student3 = {**student2, **student1}
student1.update(student2)
print(student3)
print(student2)
print(student1)
