from datetime import datetime
import random
import re


"""Перше завдання 
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою."""

def get_days_from_today(date):
    
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        nowDitetime = datetime.today()
        return date_obj.toordinal() - nowDitetime.toordinal()
    except ValueError:
        return print("Шановні! попрошу в форматі (Рік-місяць-день)")
        

# print(get_days_from_today("2021.10.09"))


"""Друге завдання
 Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних 
 випадкових чисел для таких лотерей."""

def get_numbers_ticket(min, max, quantity):
    numberList = set()

    if not (1 <= min <= max <= 1000):
        return list(numberList)
    else:
        while len(numberList) <= quantity: 
            numberList.add(random.randint(min, max))
        return sorted(list(numberList))
    

print(get_numbers_ticket(min=10, max=20, quantity=5))

"""Третє завдання
"""

def clearNumber(string):
    pattern = r"[^\d]"
    replacement = ""
    number = re.sub(pattern, replacement, string)

    if not number.startswith("38"):
        newList = f"+38{number}"
    else:
        newList = f"+{number}"
        
    return newList


# print(clearNumber("067\\t123 4567"))
