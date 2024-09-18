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
"""

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


