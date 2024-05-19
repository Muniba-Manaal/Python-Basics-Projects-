import random
import string
import sys


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    guaranteed_chars = []

    if use_uppercase:
        characters += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        characters += string.digits
        guaranteed_chars.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    if len(guaranteed_chars) < length:
        password = ''.join(random.choice(characters) for _ in range(length - len(guaranteed_chars)))
        password += ''.join(guaranteed_chars)
    else:
        password = ''.join(guaranteed_chars[:length])

    random.shuffle(list(password))  # Shuffle to avoid predictable sequences
    return ''.join(password)


def get_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            print("Exiting...")
            sys.exit(0)
        if valid_options and user_input.lower() in valid_options:
            return user_input.lower()
        elif not valid_options and user_input.isdigit() and 0 < int(user_input) <= 100:
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid choice.")


def main():
    print("Welcome to the Password Generator!")
    print("You can type 'exit' at any prompt to stop the current operation or close the application.\n")

    try:
        length = get_input("Enter the length of the password (1-100): ")
        use_uppercase = get_input("Include uppercase letters? (y/n): ", ['y', 'n']) == 'y'
        use_numbers = get_input("Include numbers? (y/n): ", ['y', 'n']) == 'y'
        use_symbols = get_input("Include symbols? (y/n): ", ['y', 'n']) == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except SystemExit:
        print("\nApplication closed. Have a great day!")


if __name__ == "__main__":
    main()
