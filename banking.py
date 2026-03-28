def deposit(data, amount):
    if amount <= 0:
        print("Invalid amount! Please enter a positive value.")
        return

    data["balance"] += amount
    data["transactions"].append(f"+{amount} Deposit")
    print(f"₹{amount} deposited successfully.")


def withdraw(data, amount):
    if amount <= 0:
        print("Invalid amount! Please enter a positive value.")
        return

    if amount > data["balance"]:
        print("Insufficient balance!")
    else:
        data["balance"] -= amount
        data["transactions"].append(f"-{amount} Withdrawal")
        print(f"₹{amount} withdrawn successfully.")


def check_balance(data):
    print(f"Current Balance: ₹{data['balance']}")


def mini_statement(data):
    print("\n--- Mini Statement ---")
    
    if len(data["transactions"]) == 0:
        print("No transactions yet.")
        return

    # Show last 5 transactions
    for transaction in data["transactions"][-5:]:
        print(transaction)

    print(f"\nAvailable Balance: ₹{data['balance']}")