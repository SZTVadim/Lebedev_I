# ЗАДАНИЕ 1: Работа с множествами
fruits = {"яблоко", "банан"}
fruits.add("апельсин")
fruits.update(["груша", "виноград"])
fruits.discard("банан")
# fruits.remove("киви")
deleted_fruits = fruits.pop()
print(fruits)
print(deleted_fruits)

# ЗАДАНИЕ 2: Работа с кортежами
coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))

# ЗАДАНИЕ 3: Операции с кортежами
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]
sum_tuple = (tuple1 + tuple2)
x_tuple = (tuple1 * 3)
 a, b, c = tuple1
 new_numbers = tuple(numbers)
 first, *middle, last = new_numbers
print(sum_tuple)
print(x_tuple)
print(first)
print(middle)
print(last)
print(new_numbers)
generator_numbers = tuple(x for x in range(0, 11) if x % 2 == 0)
print(generator_numbers)
generator_numbers2 = tuple(x * x for x in range(1, 6))
print(generator_numbers2)
tuple_one = (42,)
print(tuple_one)
