def compareSalary(salary, target_country):
    country_salaries = {
        "UK": 35423,
        "USA": 56516,
        "Canada": 64000,
        "Cambodia": 5649856
    }
    
    target_currency = ""
    if target_country == "UK":
        target_currency = "GBP"
    elif target_country == "Canada":
        target_currency = "CAD"
    elif target_country == "USA":
        target_currency = "USD"
    elif target_country == "Cambodia":
        target_currency = "KHR"
    else:
        print("Error: Invalid country input.")
        return
    
    converted_salary = convertSalary(salary, target_currency)
    
    if converted_salary > country_salaries[target_country]:
        print(f"You will be rich in {target_country} with a salary of {converted_salary:.0f} {target_currency}")
    else:
        print(f"You will be poor in {target_country} with a salary of {converted_salary:.0f} {target_currency}")

def convertSalary(salary, target_currency):
    conversion_rates = {
        
        "GBP": 0.91,
        "KHR": 4847.38,
        "CAD": 1,
        "INR": 56,
        "USD": 1.18,
    }
    converted_salary = salary / conversion_rates["CAD"] * conversion_rates[target_currency]
    return converted_salary

salary = float(input("Please enter your salary in Germany: "))
target_country = input("Enter the country you want to migrate to: ")

if target_country not in ["UK", "USA", "Canada", "Cambodia"]:
    print("Error: Invalid country input.")
else:
    compareSalary(salary, target_country)
