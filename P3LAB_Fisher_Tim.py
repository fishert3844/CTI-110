# Tim Fisher
# 10/14/2024
# P3LAB
# Calculate most effiecient coin combination
print()
print()
'''
# Regular division
print(100/3)

# Floor division - returns interger portion
print(100//3)

# Modulo - returns only the remainder
print(100%3)
print(7%4)
'''

# Get amount of money from user

money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number (cents)
# May need to round this value
# money = int(money * 100)
money = round(money * 100)

if money == 0:
    print("No change")


# --------------------------------
# Get whole dollars from money amount
dollars = money // 100
if dollars >= 1:
    if dollars == 1:
        print(f"{dollars} Dollar ")
    else:
        print(f"{dollars} Dollars ")
# Remove dollar amount from money
money = money - (dollars * 100)
# --------------------------------
# Get quarters from money amount
quarters = money // 25
if quarters >= 1:
    if quarters == 1:
        print(f"{quarters} Quarter ")
    else:
        print(f"{quarters} Quarters ")
# Remove quarters from money
money = money - (quarters * 25)
# --------------------------------
# Get dime from money amount
dimes = money // 10
if dimes >= 1:
    if dimes == 1:
        print(f"{dimes} Dime ")
    else:
        print(f"{dimes} Dimes ")
# Remove dimes from money
money = money - (dimes * 10)
# --------------------------------
# Get nickles money amount
nickles = money // 5
if nickles >= 1:
    if nickles == 1:
        print(f"{nickles} Nickle  ")
    else:
        print(f"{nickles} Nickles  ")
# Remove nickles from money
money = money - (nickles * 5)
# --------------------------------
# Get dime from money amount
pennies = money // 1
if pennies >= 1:
    if pennies == 1:
        print(f"{pennies} Penny ")
    else:
        print(f"{pennies} Pennies ")

