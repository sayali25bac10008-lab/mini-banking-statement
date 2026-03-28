def show_spending_insight(data):
    transactions = data["transactions"]

    # Extract only withdrawal amounts
    expenses = []
    for t in transactions:
        if "Withdrawal" in t:
            try:
                amount = float(t.split()[0][1:])  # remove "-" sign
                expenses.append(amount)
            except:
                continue

    if len(expenses) == 0:
        print("No spending data available yet.")
        return

    # Calculate average spending
    avg_spending = sum(expenses) / len(expenses)

    print("\n--- Spending Insight (AI) ---")
    print(f"Total Transactions Analyzed: {len(expenses)}")
    print(f"Average Spending: ₹{round(avg_spending, 2)}")

    # Simple prediction
    print(f"Estimated Next Expense: ₹{round(avg_spending, 2)}")

    # Extra insight
    if avg_spending > 500:
        print("You are spending quite a lot. Try to manage your expenses.")
    else:
        print("Your spending is under control. Good job!")