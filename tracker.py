
# Project: Expense Tracker - Installment 4
# Author: Elijah Joel P. Suarez
# Description: Takes user expenses, tax rate, and budget to calculate subtotal, tax, grand total, and budget limits.

banner = "=" * 40
divider = "-" * 40

print(banner)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.\n")

print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = subtotal + amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print(divider)
print("SUMMARY")
print(f" - {item1}:\t\t${amount1}")
print(f" - {item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print(divider)
print("Made by: Elijah Joel P. Suarez | Installment 4")
