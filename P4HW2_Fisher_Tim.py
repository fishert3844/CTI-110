# Tim Fisher
# 11/03/2024
# P4HW2
# Create program to calculate employees hours and pay
# Allow program to calculate totals when finsihed.

# Make counters and totals for final print out after user types done
total_employees = 0
total_overtime_paid = 0
total_regular_paid = 0
total_gross_paid = 0


print()
while True:
    # Ask for employee's name or "Done" to terminate
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
    # Check if the user wants to terminate
    if employee_name.lower() == 'done':
        break  # Exit the loop if 'Done' is entered
        print()

    # Enter the total amount of hours worked including overtime
    hours_worked = float(input(f"How many hours did {employee_name} work: "))
    
    # Enter employee's regular rate per hour
    employee_payrate = float(input(f"What is {employee_name}'s pay rate: "))             

    # Dotted line separation bar
    print("--------------------------------")

    # Print out employee's name
    print(f"Employee name: {employee_name}")

    # Create variable that shows the maximum hours for regular hours is 40
    regular_hours = 40

    # Create variable where overtime rate is 1.5 times that of regular pay
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

    # Update totals
    total_employees += 1
    total_overtime_paid += overtime_pay
    total_regular_paid += regular_pay
    total_gross_paid += gross_pay

    print()

    # Header for hours worked, pay rate, overtime, overtime pay, regular hours, gross pay
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'Reg Hours':<12}{'Gross Pay':<12}")

    # Dotted line separation bar
    print("-----------------------------------------------------------------------------")

    # Print the actual values underneath the header title
    print(f"{hours_worked:<15}{employee_payrate:<12}{overtime_hours:<12}{overtime_pay:<15.2f}{regular_hours_worked:<12}{gross_pay:<12.2f}")
    # Create spaces inbetween each new employee loop
    print()
    print()

# After exiting the loop, print totals
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_paid:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_paid:.2f}")
print(f"Total amount paid in gross: ${total_gross_paid:.2f}")
