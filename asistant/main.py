import sys
# Персер команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd,*args

# Додавання контактів
def add_contact(args, contacts):
    try:
        name, phone = args
        if name.isdigit() or not phone.isdigit():
            return 'Ups incorrect data'
        else:
            if name in contacts:
                return "Name is taken"
            else:
                contacts[name] = phone
                return "Contacts added."
    except ValueError:
        return 'Ups incorrect data'

# Зміна контактів
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return 'User not found'
    else:
        contacts[name] = phone
        return f"Contact {name} is changes."

# Виведення контакту
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return "User not found"
    else:
        return f"Phone number {name}: {contacts[name]}"

# Вивід всіх контактів
def all(contacts):
    list = ''
    if not contacts:
        return "Contact list is clear"
    else:
        for i,k in contacts.items():
            list += f"Name: {i} number: {k}\n"
    return list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)



        if command in ["close", "exit"]:
            print("Good buy!")
            break
        elif command == "hello":
            print("How can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()