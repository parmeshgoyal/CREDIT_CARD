import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print("Expense added successfully.")

    def display_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            for expense in self.expenses:
                print(f"{expense['timestamp']} - {expense['category']}: ${expense['amount']} ({expense['description']})")

    def generate_report(self, filename="expense_report.txt"):
        if not self.expenses:
            print("No expenses to generate a report.")
        else:
            with open(filename, "w") as file:
                file.write("Expense Report\n")
                file.write("-" * 30 + "\n")
                for expense in self.expenses:
                    file.write(f"{expense['timestamp']} - {expense['category']}: ${expense['amount']} ({expense['description']})\n")
                print(f"Expense report generated successfully: {filename}")
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            description = input("Enter a description (optional): ")
            tracker.add_expense(amount, category, description)

        elif choice == "2":
            tracker.display_expenses()

        elif choice == "3":
            filename = input("Enter the filename for the report (default: expense_report.txt): ")
            tracker.generate_report(filename)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
