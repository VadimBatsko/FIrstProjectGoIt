from pathlib import Path 
import sys
from colorama import Fore


'''Перше завдання'''
def total_salary(path):
    sum_sallary = 0
    # Перевіряєм імя файлу
    try:
        # Перевірка чи це папка
        if Path(path).is_dir():
            return 'Ви обрали папку'
        # Відкриваєм файл і читаєм по рядку
        with open(path, 'r', encoding="utf-8") as test:
            one_line = test.readlines()

            # Перевіряєм чи файл пустий
            if not any(i.strip() for i in one_line):
                return "Файл пустий"
            # Ітеруємо по рядках і додаєм кожен другий елемент до sum_sallary як число
            for i in one_line:
                # Розділяєм у список
                split_text = i.strip().split(',')
                # Обробка помилок
                try:
                    sum_sallary += int(split_text[1])
                except IndexError:
                    return "Число за індеском відсутнє"
                except ValueError:
                    return "ЗП не є числом"
    except FileNotFoundError:
        return 'Файл не знайдено'
    return sum_sallary, sum_sallary // len(one_line)


'''Друге завдання'''
def get_cats_info(path):
    cats_dicts = []
    # Робимо перевірку на папку
    if Path(path).is_dir():
            return 'Ви обрали папку'
    # Перевіряєм чи правильне ім'я файлу 
    try:
        # Відкриваєм файл і читаєм по рядку
        with open(path, 'r', encoding="utf-8") as test:
            one_line = test.readlines()

            # Перевіряєм чи файл пустий
            if not any(i.strip() for i in one_line):
                return "Файл пустий"
            # Проходимо по рядках
            for i in one_line:
                # Розділяєм на список щоб мати доступ
                split_text = i.strip().split(',')
                # Перевіряєм чи є всі параметри і якщо кіт дворовий то вік невідомий.Після перевірки додаємо до ліста
                if len(split_text) == 3:
                    cats_dicts.append({"id":split_text[0], "name":split_text[1], "age":split_text[2]})
                elif len(split_text) == 2:
                    cats_dicts.append({"id":split_text[0], "name":split_text[1], "age":"Невідомо"})
            return cats_dicts
    except FileNotFoundError:
        return "Неправильне ім'я файлу"
    


        
'''Третє завдання'''
def main():
    # Перевірка директорії
    if len(sys.argv) < 2:
        user_path = ''
    else:
        user_path = sys.argv[1]

    path = Path(user_path)
#   Перевірка наявності і коректності вводу  
    if path.exists():

#       Перевірка чи це папка чи файл
        if path.is_dir():
            elements = path.iterdir()
            for i in elements:

                # Додавання кольору в файл
                match i.suffix:
                    case '.txt':
                        print (f'{Fore.RESET}{Fore.YELLOW} {i.absolute()}{Fore.RESET}')
                    case '.py':
                        print (f'{Fore.RESET}{Fore.BLUE} {i.absolute()}{Fore.RESET}')
                    case '.cfg':
                        print (f'{Fore.RESET}{Fore.RED} {i.absolute()}{Fore.RESET}')
                    case _:
                        print (f'{Fore.RESET}{Fore.BLACK} {i.absolute()}{Fore.RESET}')
        else:
            print ("is a file")
    else:
        print ('невірний шлях', path.absolute())

# if __name__ == '__main__':
#     main()