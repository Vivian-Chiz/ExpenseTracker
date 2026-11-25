print("=====Welcome To My Expense Tracker=====")
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
expense_count = len(expenses)

print("\n===== Expense Summary =====")
print(f"Total Expense Amount Spent: ${total:.2f}")
print(f"Number of Expenses: {expense_count}")

if expense_count > 0:
    average_expense = total / expense_count
    print(f"Average Expense Amount: ${average_expense:.2f}")