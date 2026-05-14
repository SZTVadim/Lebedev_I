# ЗАДАНИЕ 1: Функции и условия

def calculate_total(price, tax_percent):
    if price < 0 or tax_percent > 20:
        return "ERROR"
    else:
        return price * tax_percent / 100 + price


print(calculate_total(20, 15))


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


print(get_level(111))


# ЗАДАНИЕ 2: Функции с условиями и match/case
def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус не активен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(process_status("active"))
