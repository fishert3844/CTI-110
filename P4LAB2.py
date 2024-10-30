# Tim Fisher
# P4LAB2
# 10/30/2024
# Use a for loop and while loop to dispaly postitive multiplication table




# Create a variable to make make program run first time
run_again = "yes"

# While loop to control the entire program

while run_again == "yes":
    print()
    # Have user enter an integer
    user_num = int(input("Enter an integer: "))
    print()
    #Check if user_num is positive
    if user_num >= 0:
        # Loop to print multiplication
        for num in range(1,13):
            print(f"{user_num} * {num} = {user_num * num}")
            
        # if user num is negitive tell the user
    else:
        print("Program does not handle negative numbers")
    print()    
    run_again = input("Would you like to run the program again, yes/no? ").lower()
    
# Loop breaks
print()
print("Exiting program...")
    





