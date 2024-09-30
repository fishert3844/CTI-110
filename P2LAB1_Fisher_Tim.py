# Tim Fisher
# 09/30/2024
# P2LAB1
# Using importe library, math, and f-string


#import mathe library

import math

# Get radius from user

radius = float(input("What is the radius of the circle? "))
print()


# Calculate diameter

diameter = 2 * radius

# Display diameter
print(f"The diameter of the circle is {diameter:.1f}")
print()

# Calculate the circumference

curcumference = 2 * math.pi * radius

# Display circumference

print(f"The curcumference of the circle is {curcumference:.2f}")
print()

# Calculate area of circle

area = math.pi * (radius ** 2)

# Display area of circle

print(f"The area of the circle is {area:.3f}")
print()

