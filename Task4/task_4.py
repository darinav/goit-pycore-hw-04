def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return None
    cmd, *args = parts
    return cmd.lower(), args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input format."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input format."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        if (user_input := input("Enter a command: ")) in ("exit", "close"):
            print("Good bye!")
            break

        if parsed := parse_input(user_input):
            command, args = parsed

            match command:
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(show_phone(args, contacts))
                case "all":
                    print(show_all(contacts))
                case _:
                    print("Invalid command.")
        else:
            print("Invalid input format.")

if __name__ == "__main__":
    main()
