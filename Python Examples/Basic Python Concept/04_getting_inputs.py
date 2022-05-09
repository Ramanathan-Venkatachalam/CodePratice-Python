#input statements
name =input("Enter the Name: ")
print(name)
print(type(name))

#By default the input values are taken as string class
a= input("Enter the value of a: ")
b= input("Enter the value of b: ")
c= a+b
print("Total: ", c)
print(type(c))

#Integer Class use int
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= a+b
print("Total: ", c)
print(type(c))

#Float Class use float
a= float(input("Enter the value of a: "))
b= float(input("Enter the value of b: "))
c= a+b
print("Total: ", c)
print(type(c))

#Getting Multiple input in the Single Line
name1, name2, name3 = input("Enter the Names: ").split()
print(name1, name2, name3)
print("Name 1: ", name1)
print("Name 2: ", name2)
print("Name 3: ", name3)

name1, name2, name3 = input("Enter the Names: ").split(',')
print(name1, name2, name3)
print("Name 1: ", name1)
print("Name 2: ", name2)
print("Name 3: ", name3)