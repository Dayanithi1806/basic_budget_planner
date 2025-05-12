class BudgetPlanner:
    def __init__(self): 
        self.income = 0.0
        self.expenses = {}

    def set_income(self, amount):
        self.income = amount

    def add_expense(self, name, amount):
        if amount < 0:
            print("Expense amount cannot be negative.")
            return
        self.expenses[name] = self.expenses.get(name, 0) + amount

    def total_expenses(self):
        return sum(self.expenses.values())

    def remaining_balance(self):
        return self.income - self.total_expenses()

    def show_summary(self):
        print("\n----- Budget Summary -----")
        print(f"Income: ${self.income:.2f}")
        print("Expenses:")
        for name, amount in self.expenses.items():
            print(f"  {name}: ${amount:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")
        print(f"Remaining Balance: ${self.remaining_balance():.2f}")

def main():
    planner = BudgetPlanner()

    while True:
        try:
            income = float(input("Enter your monthly income: $"))
            if income < 0:
                print("Income cannot be negative. Try again.")
                continue
            planner.set_income(income)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        choice = input("\nAdd an expense? (yes/no): ").strip().lower()
        if choice == 'no':
            break
        elif choice == 'yes':
            name = input("Expense name: ").strip()
            try:
                amount = float(input(f"Amount for {name}: $"))
                planner.add_expense(name, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Please type 'yes' or 'no'.")

    planner.show_summary()

if __name__ == "__main__":
    main()
