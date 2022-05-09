class User:
    #Class Attribute
    course = "Python"

#Creating a instance/object
obj=User()
print(User.__dict__) #Here it have main module and its class attribute
print(User.course) #Printing the class attribute

print(obj.__dict__) #Here the dictionary will be empty
print(obj.course) #Printing the instance attribute
#It will print "Python" becoz first it checks his dictionary since its empty it goes up the class dictionary and gets the class attribute from their and print it

obj.course = "C" #Assigning the instance attribute. In the above step the instance dictionary is empty now we have added a instance variable it will be assigned to its dictionary and therw will be no change in the class dictionary.
print(obj.__dict__)
print(obj.course) #Printing the instance attribute

obj2 = User()
print(obj2.course)