# Tim Fishr
# 10/14/2024
# P3HW1
# Creating a program that has Branching to creat letter grade


# Tim Fisher
# 10/09/2024
# P2HW2
# Design a program were users enter grades store grades add it as a comment block
print()
print()
#Create variables for Grade List

Module1 = float(input('Enter grade for Module 1: '))
Module2 = float(input('Enter grade for Module 2: '))
Module3 = float(input('Enter grade for Module 3: '))
Module4 = float(input('Enter grade for Module 4: '))
Module5 = float(input('Enter grade for Module 5: '))
Module6 = float(input('Enter grade for Module 6: '))

grade_list = [Module1, Module2, Module3, Module4, Module5, Module6]

print()

print("------------Results------------")

print(f"{'Lowest Grade:':<22} {min(grade_list):<25}")
print(f"{'Highest Grade:':<22} {max(grade_list):<25}")
print(f"{'Sum of Grades:':<22} {sum(grade_list):<25}")
print(f"{'Average:':<22} {sum(grade_list)/len(grade_list):<25.2f}")


print("-------------------------------")

# Create average grade variable

average = sum(grade_list)/len(grade_list)

# Create branching to get letter grade

if average >= 90:
    lettergrade = "A"

elif average >= 80:
    lettergrade = "B"

elif average >= 70:
    lettergrade = "C"

elif average >= 60:
    lettergrade = "D"

else:
    lettergrade = "F"

print(f"Your grade is: {lettergrade}")



















        
