print("=====My Expense Tracker=====")
expenses = []
while True:
    expense_name = input("Enter expense name (or type done to exit) : ")
    if expense_name.lower() == 'done':
        break
    
    try:
        expense_amount = float(input("Enter expense amount: $"))
        if expense_amount <= 0:
            print("Please enter a valid amount greater than zero.")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    expenses.append((expense_name, expense_amount))
    print("Expenses added!")
total = sum(amount for name, amount in expenses)

print("\n===== Expense Summary =====")
print(f"Total Amount Spent: ${total:.2f}")