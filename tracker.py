# Project: Expense Tracker - Installment 5
# Author: Elijah Joel P. Suarez
# Description: Menu-driven tracker that adds expenses, shows totals, and exits.

banner = "=" * 40
divider = "-" * 40

print(banner)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print(banner)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

        subtotal = subtotal + amount
        count = count + 1

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand total:\t${total}")

        if over_budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.90:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print(divider)
        print("Made by: Elijah Joel P. Suarez | Installment 5")
        print(banner)

    else:
        print("  Please choose 1, 2, 3 or 4.")