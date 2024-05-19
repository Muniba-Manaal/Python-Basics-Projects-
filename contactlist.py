import sys
import re

# The contact list will be stored in a dictionary.
contacts = {}


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_phone(phone):
    pattern = r"^\+?1?\d{9,15}$"  # Simple regex for international phone numbers
    return re.match(pattern, phone) is not None


def get_input(prompt, validation_func=None, allow_blank=False):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            print("Exiting the current operation.")
            return None
        if allow_blank and user_input == '':
            return None
        if not validation_func or validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again or type 'exit' to cancel.")


def add_contact():
    name = get_input("Enter the contact's name (or type 'exit' to cancel): ")
    if not name:
        return
    if name in contacts:
        print("Contact already exists.")
        return

    email = get_input("Enter the contact's email: ", validate_email)
    if not email:
        return

    phone = get_input("Enter the contact's phone number: ", validate_phone)
    if not phone:
        return

    contacts[name] = {'Email': email, 'Phone': phone}
    print(f"Contact '{name}' added.")


def edit_contact():
    old_name = get_input("Enter the name of the contact to edit (or type 'exit' to cancel): ")
    if not old_name or old_name not in contacts:
        print("Contact not found or operation cancelled.")
        return

    new_name = get_input("Enter the new name (leave blank to keep current): ", allow_blank=True)
    email = get_input("Enter the new email (leave blank to keep current): ", validate_email, allow_blank=True)
    phone = get_input("Enter the new phone number (leave blank to keep current): ", validate_phone, allow_blank=True)

    contact_info = contacts.pop(old_name)
    contacts[new_name if new_name else old_name] = {
        'Email': email if email is not None else contact_info['Email'],
        'Phone': phone if phone is not None else contact_info['Phone']
    }
    print(f"Contact '{old_name}' updated.")


def delete_contact():
    name = get_input("Enter the name of the contact to delete (or type 'exit' to cancel): ")
    if not name or name not in contacts:
        print("Contact not found or operation cancelled.")
        return

    del contacts[name]
    print(f"Contact '{name}' deleted.")


def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"{name} - Email: {details['Email']}, Phone: {details['Phone']}")


def exit_program():
    print("Exiting the program.")
    sys.exit(0)


def main():
    actions = {
        '1': add_contact,
        '2': edit_contact,
        '3': delete_contact,
        '4': list_contacts,
        '5': exit_program,
    }

    while True:
        print("\n--- Contact List Application ---")
        print("1 - Add a new contact")
        print("2 - Edit an existing contact")
        print("3 - Delete a contact")
        print("4 - List all contacts")
        print("5 - Exit")
        choice = get_input("Choose an action (or type 'exit' to close the app): ")

        if choice and choice in actions:
            actions[choice]()
        elif not choice:
            break  # Exit the application if 'None' is returned from get_input
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
