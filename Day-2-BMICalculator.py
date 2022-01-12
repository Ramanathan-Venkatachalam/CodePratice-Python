#BMI Calculator

print("Welcome to BMI Calculator")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))
print(type(weight))

#Type-casting
new_height = float(height)
new_weight = int(weight) 

#BMI Formula
bmi = new_weight / new_height ** 2
print(type(bmi))
print(bmi)

#BMI to whole number
bmi_as_int = int(bmi)
print(type(bmi_as_int))
print(bmi_as_int)