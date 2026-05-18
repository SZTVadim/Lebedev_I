# ЗАДАНИЕ 1: Класс Book (Книга)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"{self.title}, {self.author}, {self.pages}"

    def is_long(self):
        if self.pages > 300:
            return "True"
        else:
            return "False"


book1 = Book("Одиссея", "Кристофер Нолан", 450)
book2 = Book("Гарри Поттер", "Роулинг", 766)
book3 = Book("Золотая рыбка", "А.С. Пушкин", 130)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
print(book1.is_long())
print(book2.is_long())
print(book3.is_long())


# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Пополнение баланса на {amount} баланс {self.balance}"

    def withdraw(self, amount):
        self.balance = self.balance
        if self.balance >= amount:
            self.balance -= amount
            return f"Успешное списание на сумму {amount}, Ваш баланс {self.balance}"
        else:
            return "Недостаточно средств"

    def balances(self):
        return f"Ваш баланс - {self.balance}"


score = BankAccount("Igor", 500)
print(score.balances())
print(score.deposit(200))
print(score.withdraw(500))
print(score.balances())
