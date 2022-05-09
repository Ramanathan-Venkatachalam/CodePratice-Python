#Instance Methods
class Players:
    #Class Attribute
    name = 'PV Sindhu'
    age = 26
    sports = 'Badminton'

    #Function/Methods
    def printall(self,gender):
        print('Name= ', Players.name)
        print('Age= ', Players.age)
        print('Sports= ', Players.sports)
        print('Gender= ', gender)

obj=Players() #Creating a instance/object
print(Players.__dict__)

print(obj.__dict__)#Here the dictionary will be empty
obj.printall() #Printing the instance methods (frequently used)
#It will print 'printall' function contents becoz first it checks his dictionary since its empty it goes up the class dictionary and gets the class attribute from their and print it

#Other ways to access the Instance Methods
#Syntax = ClassName.MethodName(ObjectName)
Players.printall(obj)

#We shall also add the extra parameter to the Class Methods printall
obj.printall('Female')
Players.printall(obj,'Female')