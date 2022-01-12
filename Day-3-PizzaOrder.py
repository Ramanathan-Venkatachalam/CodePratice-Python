#PizzaOrder
print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Yes or No :")
extra_cheese = input("Do you want extra cheese? Yes or No :")

if size == "S":
  bill = 100
elif size == "M":
  bill = 250
else:
  bill = 500

if add_pepperoni == "Yes":
  if size == "S":
    bill += 25
  else:
    bill += 50

if extra_cheese == "Yes":
  bill += 10

print(f"Your final bill is: Rs.{bill}")