from colorama import Fore
from decorators import input_error


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
def show_phone(args, contacts):
    phone = args[0]
    return contacts[phone]


def show_contacts(contacts):
    result = ""
    for username, phone in contacts.items():
        result += f"\n{username}: {phone}" if result else f"{username}: {phone}"

    return f"All contacts:\n{result}"

@input_error
def main():
    contacts = {}
    print("Hello, I your assistent, enter command")

    while True:
        user_input = input(f"{Fore.BLUE}[Assistent]{Fore.RESET} > ")

        if not user_input or user_input.isspace():
            continue

        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_contacts(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
