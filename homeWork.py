from datetime import datetime
import random
import re


"""Перше завдання 
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою."""

def get_days_from_today(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    nowDitetime = datetime.today()
    return date_obj.toordinal() - nowDitetime.toordinal()

# print(get_days_from_today("2021-10-09"))


"""Друге завдання
 Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних 
 випадкових чисел для таких лотерей."""

def get_numbers_ticket(min, max, quantity):
    numberList = set()

    # Перевірка валідності:
    #min - не менше 1.
    #max - не більше 1000.
    #quantity - значення між min і max.

    if not (1 <= min <= max <= 1000 and min <= quantity <= max):
        return list(numberList)
    else:
        while len(numberList) <= quantity: 
            numberList.add(random.randint(min, max))
        return sorted(list(numberList))
    

# print(get_numbers_ticket(min=1, max=49, quantity=6))

"""Третє завдання

1 зробити чисті номери
2 перевірити чи є 38 на початку
3 додати до номерів +38
"""

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def clearNumber(list):
    pattern = r"[^\d]"
    replacement = ""
    newList = []

    for i in list:
        number = re.sub(pattern, replacement, i)

        if not number.startswith("38"):
            number = f"+38{number}"
        else:
            number = f"+{number}"

        newList.append(number)
    return newList


print(clearNumber(raw_numbers))  