# Tim Fisher
# 10-23-2024
# P3HW2
# Calculate regular and overtime pay for employee
'''
input: get name

float(inpu: enter hours
float(input: get reg pay rate

print ------
print employees name

if: employees has overtime(hours worked greater > 40
calculation of hours (hours worked - 40)
calculate pay rate (regular pay * 1.5)
Determine hours worked - has to be 40
calculate pay for reg hours (hours worked * reguar pay)
calculate pay for overtime (ot hours * ot pay rate)
calculate gross pay (reg pay + overtime pay)

else: (has no overtime)
hours worked is (original hours worked)
pay rate (original pay rate)
OT hours is 0
OT pay rate is 0
calculate pay for reg hours (hours worked * reguar pay)
'''
print()
# Enter employee's name
employee_name = input("Enter employee's name: ")

# Enter the total amount of hours worked including over time
hours_worked = float(input("Enter number of hours worked: "))

# Enter employee's regular rate per hour                    
employee_payrate = float(input("Enter employee's pay rate: "))             

# Dotted line seperation bar
print("--------------------------------")

# Print out employee's name
print(f"Employee name: {employee_name}")

# Create Variable that shows the maximum hours for reg hours is 40
regular_hours = 40

# Create variable were over time rate is 1.5 times that of regular pay
overtime_rate = 1.5

# Calculate overtime hours and regular hours
if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    regular_hours_worked = regular_hours
else:
    overtime_hours = 0
    regular_hours_worked = hours_worked

# Calculate regular pay, overtime pay, and gross pay
regular_pay = regular_hours_worked * employee_payrate
overtime_pay = overtime_hours * employee_payrate * overtime_rate
gross_pay = regular_pay + overtime_pay

print()

# Header for hours worked, pay rate, overtime, overtime pay, regular hours, gross pay
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'Reg Hours':<12}{'Gross Pay':<12}")

# Dotted line separation bar
print("----------------------------------------------------------------------------")

# Print the actual values underneath the header title
print(f"{hours_worked:<15}{employee_payrate:<12}{overtime_hours:<12}{overtime_pay:<15.2f}{regular_hours_worked:<12}{gross_pay:<12.2f}")

input()







