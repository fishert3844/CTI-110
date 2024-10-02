# Tim Fisher
# 10-02-2024
# P2LAB2
# Write a program that creates a dictionary where the key and value pairs


# Mpg dictionary

cars_mpg = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

# Print all keys in dictionary

print(cars_mpg.keys())
print()

# Get a car key from user

userCar = input("Enter a vehicle to seee it's mpg: ")
print()
# Display mpg of vehicle entered

print(f"The {userCar} gets {cars_mpg[userCar]} mpg.")
print()

# Enter miles to be driven

milesDriven = float(input(f"How many miles will you drive the {userCar}? "))
print()

# Calculate gas needed

gallonsNeeded = milesDriven/cars_mpg[userCar]

# Display gallons needed

print(f"{gallonsNeeded:.2f} gallon(s) of gas are needed to drive the {userCar} {milesDriven} miles.")
