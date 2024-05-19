import csv


class ExpenseTracker:
    def __init__(self):
        self.accounts_file = 'accounts.csv'  # CSV file to store user accounts
        self.accounts = self.load_accounts()  # Load accounts from the CSV file
        self.current_user = None  # To keep track of the logged in user

    def load_accounts(self):
        """Load user accounts from the CSV file."""
        accounts = {}
        try:
            with open(self.accounts_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password, balance = row
                    accounts[username] = {
                        'password': password,
                        'balance': float(balance)
                    }
            return accounts
        except FileNotFoundError:
            return {}

    def save_accounts(self):
        """Save user accounts to the CSV file."""
        with open(self.accounts_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for username, info in self.accounts.items():
                writer.writerow([username, info['password'], info['balance']])

    def create_account(self, user_name, password, initial_balance):
        """Create a new user account."""
        if user_name in self.accounts:
            return "User already exists."
        self.accounts[user_name] = {
            'password': password,
            'balance': initial_balance
        }
        self.save_accounts()
        return "Account created successfully."

    def login_user(self, user_name, password):
        """Login a user."""
        while True:
            if user_name in self.accounts and self.accounts[user_name]['password'] == password:
                self.current_user = user_name
                return "Login successful."
            else:
                print("Invalid username or password.")
                user_name = input("Enter username: ")
                password = input("Enter password: ")

    def update_balance(self, amount):
        """Update the balance of the current user."""
        if self.current_user:
            self.accounts[self.current_user]['balance'] += amount
            self.save_accounts()
            return "Balance updated successfully."
        else:
            return "No user is logged in."

    def check_balance(self):
        """Check the balance of the current user."""
        if self.current_user:
            return f"Current Balance: {self.accounts[self.current_user]['balance']}"
        else:
            return "No user is logged in."

    def logout(self):
        """Logout the current user."""
        self.current_user = None
        return "Logout successful."


def run_app():
    app = ExpenseTracker()
    while True:
        if app.current_user:
            print("\nMenu:")
            print("1. Update Balance")
            print("2. Check Balance")
            print("3. Logout")
            print("4. Exit App")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount (use negative for expense, positive for income): "))
                print(app.update_balance(amount))
            elif choice == "2":
                print(app.check_balance())
            elif choice == "3":
                print(app.logout())
            elif choice == "4":
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please try again.")
        else:
            print("\nMain Menu:")
            print("1. Login")
            print("2. Create Account")
            print("3. Exit App")
            choice = input("Enter your choice: ")

            if choice == "1":
                user_name = input("Enter username: ")
                password = input("Enter password: ")
                print(app.login_user(user_name, password))
            elif choice == "2":
                user_name = input("Enter username: ")
                password = input("Enter password: ")
                initial_balance = float(input("Enter initial balance: "))
                print(app.create_account(user_name, password, initial_balance))
            elif choice == "3":
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please try again.")


# Uncomment the line below to run the application
run_app()
