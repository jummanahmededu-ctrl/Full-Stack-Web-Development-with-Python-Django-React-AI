FILE = "expenses.txt"

def add_expense():
    try:
        expense_id = input("Expense ID: ")
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        description = input("Description: ")
        amount = float(input("Amount: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
        with open(FILE, "a") as file:
            file.write(f"{expense_id},{date},{category},{description},{amount}\n")
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def view_expenses():
    try:
        with open(FILE, "r") as file:
            expenses = file.readlines()
            if len(expenses) == 0:
                print("No expenses available.")
                return
            for expense in expenses:
                data = expense.strip().split(",")
                print("-" * 40)
                print("Expense ID :", data[0])
                print("Date :", data[1])
                print("Category :", data[2])
                print("Description :", data[3])
                print("Amount :", data[4])
                print("-" * 40)
    except FileNotFoundError:
        print("No expense records found.")


def search_expense():
    expense_id = input("Enter Expense ID to search: ")
    try:
        with open(FILE, "r") as file:
            expenses = file.readlines()
            if len(expenses) == 0:
                print("No expenses available.")
                return
            found = False
            for expense in expenses:
                data = expense.strip().split(",")
                if data[0] == expense_id:
                    print("\nExpense Found")
                    print("Expense ID :", data[0])
                    print("Date :", data[1])
                    print("Category :", data[2])
                    print("Description :", data[3])
                    print("Amount :", data[4])
                    found = True
                    break
            if not found:
                print("Expense not found.")
    except FileNotFoundError:
        print("No expense records found.")

def update_expense():
    expense_id = input("Enter Expense ID to update: ")
    try:
        with open(FILE, "r") as file:
            expenses = file.readlines()
        if len(expenses) == 0:
            print("No expenses available.")
            return
        updated = False
        for i in range(len(expenses)):
            data = expenses[i].strip().split(",")
            if data[0] == expense_id:
                print("Enter new information")
                date = input("New Date: ")
                category = input("New Category: ")
                description = input("New Description: ")
                try:
                    amount = float(input("New Amount: "))
                    if amount < 0:
                        print("Amount cannot be negative.")
                        return
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    return
                expenses[i] = (
                    f"{expense_id},{date},{category},{description},{amount}\n"
                )
                updated = True
                break
        if updated:
            with open(FILE, "w") as file:
                file.writelines(expenses)
            print("Expense updated successfully.")
        else:
            print("Expense not found.")
    except FileNotFoundError:
        print("No expense records found.")

def delete_expense():
    expense_id = input("Enter Expense ID to delete: ")
    try:
        with open(FILE, "r") as file:
            expenses = file.readlines()
        if len(expenses) == 0:
            print("No expenses available.")
            return
        new_expenses = []
        deleted = False
        for expense in expenses:
            data = expense.strip().split(",")
            if data[0] != expense_id:
                new_expenses.append(expense)
            else:
                deleted = True
        if deleted:
            with open(FILE, "w") as file:
                file.writelines(new_expenses)
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")
    except FileNotFoundError:
        print("No expense records found.")

def expense_summary():
    try:
        with open(FILE, "r") as file:
            expenses = file.readlines()
        if len(expenses) == 0:
            print("No expenses available.")
            return
        amounts = []
        for expense in expenses:
            data = expense.strip().split(",")
            amounts.append(float(data[4]))
        total_expenses = len(amounts)
        total_spending = sum(amounts)
        average_expense = total_spending / total_expenses
        highest_expense = max(amounts)
        lowest_expense = min(amounts)

        print("\n========= Expense Summary =========")
        print("Total Expenses :", total_expenses)
        print("Total Spending :", total_spending, "BDT")
        print("Average Expense :", round(average_expense, 2), "BDT")
        print("Highest Expense :", highest_expense, "BDT")
        print("Lowest Expense :", lowest_expense, "BDT")
    except FileNotFoundError:
        print("No expense records found.")

def main():
    while True:
        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Expense Summary")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            update_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            expense_summary()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")
main()