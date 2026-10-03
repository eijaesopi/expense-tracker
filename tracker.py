# Project: Expense Tracker - Installment 2
# Author: Elijah Joel P. Suarez
# Description: Takes user input for two expenses, calculates total and average, and displays a summary.

banner = "=" * 40
divider = "-" * 40

print(banner)

print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.\n")

print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print(divider)
print("SUMMARY")
print(f"  - {item1}:\t\t${amount1}")
print(f"  - {item2}:\t\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print(divider)

print(f"Made by: Elijah Joel P. Suarez  |  Installment 2")