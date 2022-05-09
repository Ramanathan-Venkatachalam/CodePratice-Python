#Type Casting
"""
By default all data types in python are class
There are 3 constructor that shall be used in type casting
1. int()
2. float()
3. str()
"""

q = 10
print(q)
print(type(q))

a = 11.0
print(a)
b = int(a)
print(b)
print(type(a))
print(type(b))

a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= a+b
print("Total: ", c) #Print the addition value
print(type(c))

a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= a+b
print("Total: " + str(c)) #Concatenation
print(type(c))