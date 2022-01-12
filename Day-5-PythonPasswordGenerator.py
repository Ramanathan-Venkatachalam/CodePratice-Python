#PasswordGenerator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password_list?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
password = ""
for char in range(1, nr_letters+1):
  #random_char = random.choice(letters)
  #password = password + random_char
  password += random.choice(letters)

for char in range(1, nr_numbers+1):
  #random_num = random.choice(numbers)
  #password = password + random_num
  password += random.choice(numbers)

for char in range(1, nr_symbols+1):
  #random_sym = random.choice(symbols)
  #password = password + random_sym
  password += random.choice(symbols)

print(password)
"""
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(1, nr_letters+1):
  #random_char = random.choice(letters)
  #password_list = password_list + random_char
  password_list.append(random.choice(letters))
  #password_list += random.choice(letters)

for char in range(1, nr_numbers+1):
  #random_num = random.choice(numbers)
  #password_list = password_list + random_num
  password_list += random.choice(numbers)

for char in range(1, nr_symbols+1):
  #random_sym = random.choice(symbols)
  #password_list = password_list + random_sym
  password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password = password + char
print(f"The random password is: {password}")