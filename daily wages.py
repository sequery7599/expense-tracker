import math

wage = float(input("Enter your hourly wage: "))
work = float(input("Enter how many hours you worked: "))
day = input("What day is it?")
wages = wage * work

print(f"Hourly wage: {wage}")
print(f"Hours worked: {work}")
print(day)

if day == "Sunday":
    new_wage = wages * 2
    print(new_wage)
else:
    print(wages)