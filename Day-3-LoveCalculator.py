#LoveCalculator
print("Welcome to the Love Score Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1 + name2
lower_case_names = combined.lower()
T = lower_case_names.count("t")
R = lower_case_names.count("r")
U = lower_case_names.count("u")
E = lower_case_names.count("e")
true = T+R+U+E
L = lower_case_names.count("l")
O = lower_case_names.count("o")
V = lower_case_names.count("v")
E = lower_case_names.count("e")
love = L+O+V+E

love_score = int(str(true) + str(love))

if love_score > 90:
    print(f"Your score is {love_score}, you both are a perfect match.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
elif love_score <= 30:
    print(f"Your score is {love_score}, you both are like CAT and RAT together")
else:
    print(f"Your score is {love_score}.")