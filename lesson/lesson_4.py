# ЗАДАНИЕ 1: Работа с типами данных

string = "Привет"
number = 42
number_float = 3.14
lesson_list = [1, 2, 3]
print(type(string))
print(type(number))
print(type(number_float))
print(type(lesson_list))

# ЗАДАНИЕ 2: Преобразование регистра строк

string_register = "python PROGRAMMING"
conversion_lower = string_register.lower()
conversion_upper = string_register.upper()
conversion_first = string_register.capitalize()
conversion_title = string_register.title()
print(conversion_lower)
print(conversion_upper)
print(conversion_first)
print(conversion_title)

# ЗАДАНИЕ 3: Удаление пробелов
string_hello = "  Hello World  "
print(string_hello)  # Для примера, что пробелы убрались как я хотел
delete_string_hello = string_hello.strip()
delete_string_left = string_hello.lstrip()
delete_string_right = string_hello.rstrip()
print(delete_string_hello)
print(delete_string_left)
print(delete_string_right)

# ЗАДАНИЕ 4: Разделение и объединение строк
list_level4 = "яблоко,банан,апельсин,груша"
strip_list = list_level4.split(",")
replace_list = " | ".join(strip_list)
print(strip_list)
print(replace_list)

# ЗАДАНИЕ 5: Замена подстрок
text_level5 = "Я изучаю Python. Python - это круто!"
new_text_level5 = text_level5.replace("Python", "Java")
print(new_text_level5)

# ЗАДАНИЕ 6: Поиск и подсчет
index_lesson = "Python программирование на Python"
text_index_lesson = index_lesson.find("Python")
count_index_lesson = index_lesson.count("Python")
proverka_index_lesson = index_lesson.find("Java")
print(text_index_lesson)
print(count_index_lesson)
print(proverka_index_lesson)

# ЗАДАНИЕ 7: Проверка типа символов
number_count_hello = "Hello123"
number_count = "12345"
hello_count = "Hello"
space_count = "  "
print(number_count_hello.isalnum())
print(number_count.isdigit())
print(hello_count.isalpha())
print(space_count.isspace())

# ЗАДАНИЕ 8: Срезы строк
python_very_good = "Python very good"
srez_python_very_good = python_very_good[0:3]
srez_python_last = python_very_good[-3:]
srez_python_step = python_very_good[::2]
srez_reverse = python_very_good[::-1]
print(srez_python_very_good)
print(srez_python_last)
print(srez_python_step)
print(srez_reverse)

# ЗАДАНИЕ 9: Экранирование символов
say_hello = "Он сказал: \"Привет\""
print(say_hello)
one_two = "Первая строка \nВторая строка"
print(one_two)
