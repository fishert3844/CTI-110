# Tim Fisher
# 11/13/2024
# P5LAB
# Simulate self-checkout machine using functions



# Import random library
import random


def disperse_change(money):
    print(f"Change is: ${money:.2f}")
    print()
    
    # Convert money to integer
    # money = int(money * 100)
    money = int(round(money * 100, 2))

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
    # Get disperse_changedime from money amount
    pennies = money // 1
    if pennies >= 1:
        if pennies == 1:
            print(f"{pennies} Penny ")
        else:
            print(f"{pennies} Pennies ")




def main():
    print("Welcome to the store!")
    # Generate money owed
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")
    inPut = float(input("How much cash will you put in the self-checkout? $"))
    change = inPut - owed
    change_owed = round(change, 2)
    
     
    # Call the function to show the change as coins
    disperse_change(change_owed)

    
# Call the main
if __name__ == "__main__":
    main()
