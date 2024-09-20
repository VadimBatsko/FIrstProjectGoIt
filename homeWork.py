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
        




"""Друге завдання
 Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних 
 випадкових чисел для таких лотерей."""

def get_numbers_ticket(min, max, quantity):
    numberList = set()

    if not (1 <= min <= max <= 1000 and (max - min) >= quantity >= 0):
        return list(numberList)
    else:
        while len(numberList) < quantity: 
            numberList.add(random.randint(min, max))
        return sorted(list(numberList))
    
print(get_numbers_ticket(10, 15, 5))


"""Третє завдання
"""

def normalize_phone(phone_number):
    pattern = r"[^\d]"
    replacement = ""
    number = re.sub(pattern, replacement, phone_number)

    if not number.startswith("38"):
        newList = f"+38{number}"
    else:
        newList = f"+{number}"
        
    return newList



