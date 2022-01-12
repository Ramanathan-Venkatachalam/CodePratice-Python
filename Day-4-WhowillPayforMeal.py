#PayforMeal
names_string = input("Give me everybody's names, separated by a comma. ")

#splitfunction()
names = names_string.split(", ")

import random
length_of_list = len(names)
random_pick = random.randint(0, length_of_list-1)
print(f"{names[random_pick]} is going to buy the meal today!")