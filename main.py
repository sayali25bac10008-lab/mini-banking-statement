import json
from banking import deposit, withdraw, check_balance, mini_statement
from ml_model import show_spending_insight

DATA_FILE = "data.json"

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {"balance": 0, "transactions": []}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def main():
    data = load_data()

    while True:
        print("\n====== Mini Banking System ======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Mini Statement")
        print("5. Spending Insight (AI)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            deposit(data, amount)
            save_data(data)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(data, amount)
            save_data(data)

        elif choice == "3":
            check_balance(data)

        elif choice == "4":
            mini_statement(data)

        elif choice == "5":
            show_spending_insight(data)

        elif choice == "6":
            save_data(data)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()