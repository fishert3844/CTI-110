# Tim Fisher
# 09/23/2024
# P1HW2
# Write program Pseudocode (logic) and add it as a comment block to the submitted program


# Explains what the program does

print("This program calculates and displays travel expenses\n")

# Enter the budget amount

budget = int(input("Enter Budget: "))
print()

# Where the client is traveling to

destination = input("Enter your travel destination: ")
print()

# Estimated cost for fuel

gas = int(input("How much do you think you will spend on gas? "))
print()
#  Cost for Housing

housing = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# Cost for food

food = int(input("Last, how much do you need for food? "))
print() 

# Show itemized list of items with a remaining balance

print("------------Travel Expenses------------")

print(f"{'Location:':<22}{destination:<25}")
print(f"{'Initial Budget:':<22}${budget:<25,.2f}")
print(f"{'Fuel:':<22}${gas:<25,.2f}")
print(f"{'Accomodation:':<22}${housing:<25,.2f}")
print(f"{'Food:':<22}${food:<25,.2f}")
print("-" * 39)
print()
remaining_balance = budget - gas - housing - food 
print(f"{'Remaining Balance:':<22}${remaining_balance:<25,.2f}")
input()
