month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = input(
    "Enter the year as two numerical digits (for example: 98, 20, 21): ")

# checking for month input
if month < 1 or month > 12:
    print("Error: Invalid Month Input")

# Checking for year input
elif not year.isdigit() or len(year) != 2:
    print("Error: Invalid Year Input")

    # Checking for day input
elif day < 1 or day > 31:
    print("Error: Invalid Day Input")

# Print success if everything is valid
else:
    print(f"Success: Congratulations! you entered the correct date. {month}/{day}/{year}")
