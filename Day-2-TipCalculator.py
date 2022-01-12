#BillTipCalculator
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? Rs:")
total_bill_as_float = float(total_bill)

#TipPercentageCalculation
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
percent_tip_as_int = int(percent_tip)
total_tip = percent_tip_as_int / 100 * total_bill_as_float + total_bill_as_float

#TotalnoofPeople
no_of_people = input("How many people to split the bill?")
no_of_people_as_int = int(no_of_people)

#Each person should pay
each_person_pay = total_tip / no_of_people_as_int
round_of_pay = (round(each_person_pay, 2))
print(f"Each person should pay: Rs:{round_of_pay}")