import random


def number_guessing_game():

    print("\nChoose your difficulty level:")
    print("1. Easy (1-10) - 5 attempts")
    print("2. Medium (1-50) - 10 attempts")
    print("3. Hard (1-100) - 15 attempts")
    print("You can exit the game at any time by typing 'exit'.")

    while True:
        difficulty = input("Enter your choice (1/2/3 or 'exit' to quit): ").strip()

        if difficulty.lower() == 'exit':
            print("\nYou've chosen to exit the game. See you next time!")
            return

        if difficulty not in ["1", "2", "3"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        attempts_allowed = {"1": 5, "2": 10, "3": 15}[difficulty]
        range_max = {"1": 10, "2": 50, "3": 100}[difficulty]
        break

    number_to_guess = random.randint(1, range_max)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {range_max}. Can you guess it? You have {attempts_allowed} attempts.")

    while attempts < attempts_allowed:
        guess_input = input(f"\nAttempt {attempts + 1}/{attempts_allowed} - Enter your guess (or type 'exit' to quit): ").strip()

        if guess_input.lower() == 'exit':
            print("\nYou've chosen to exit the game. See you next time!")
            return

        try:
            guess = int(guess_input)
            if guess < 1 or guess > range_max:
                print(f"Oops! Your guess should be within the range 1 to {range_max}. Try again.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Keep trying.")
            elif guess > number_to_guess:
                print("Too high! Keep trying.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts. Well done!")
                break
        except ValueError:
            print("That doesn't seem like a number. Please enter a valid number.")

        if attempts == attempts_allowed:
            print(f"\nSorry, you've run out of attempts. The number was {number_to_guess}.")

    # Asking if the user wants to play again with proper validation
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again in ["yes", "no"]:
            break
        print("Invalid response. Please answer 'yes' or 'no'.")

    if play_again == "yes":
        number_guessing_game()
    else:
        print("\nThank you for playing the Number Guessing Game!")


def main():
    print("\nWelcome to the Number Guessing Game!")
    print("In this game, you'll try to guess a number that I'm thinking of.")
    number_guessing_game()


if __name__ == "__main__":
    main()
