#LifeRemaining Calculator

age = input("What is your current age?")
#Type-casting
current_age = int(age)
print(current_age)

#LifeRemaining
years_left = 90 - current_age

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

#PrintingResult
result = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(result)