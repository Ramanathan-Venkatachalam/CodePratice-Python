a=10
b=10
c=a+b
print('Total: ', c)

#Type of Variable
print(type(a))
print(type(b))
print(type(c))

#Memory Address of Variable
#Python allocates memory address based on variable values
#If the values are same then they are mapped with sane memory address and vice-versa
print(id(a))
print(id(b))
print(id(c))

a=11
b=12
c=a+b
print('Total: ', c)
print(id(a))
print(id(b))
print(id(c))