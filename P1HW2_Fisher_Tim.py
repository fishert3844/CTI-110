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

print("-------------Travel Expenses------------")

print("Location:", destination)
print(f"Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation;", housing)
print("Food:", food)
print()
remaining_balance = budget - gas - housing - food 
print("Remaining Balance:", remaining_balance) 
      
