class car():
    pass
#In python all are classes and objects
#a is object
a=10

print(type(a))
#a is the object of class 'int'

print(type(car))
#car is the object of class 'type'


swift=car()
#swift is the object

print(isinstance(swift,car))
#To find whether the swift is the object/instance of the class car we shall use isinstance function
#If the result is True then its a instance of that class
print(isinstance(a,int))

print(type(swift))
#Its shows that the swift object belongs to the car class in main program
