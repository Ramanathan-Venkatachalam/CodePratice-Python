#Class Methods
class Players:
    #Class Attribute
    name = 'Rahul Dravid'
    age = 48
    sports = 'Cricket'

    #Function/Methods
    def printall():
        print('Name= ',Players.name)
        print('Age= ',Players.age)
        print('Sports= ',Players.sports)

#Accessing the Class Methods
#Syntax = ClassName.FunctionName() (frequently used)
Players.printall() #Print the content inside the function
print(Players.__dict__)
#If you see here the Class dictionary would have created a printall attribute and assigned a space-address 'printall': <function Players.printall at 0x00000143DEA5D280>

#Other ways to access the Class Methods
#1.Using getattr inbuild function
print(getattr(Players, 'printall')) #Prints the address
getattr(Players, 'printall')() #Prints the value inside the function

#2.Usind a __dict__
#Syntax= ClassName.__dict__, ['VariableName']()
Players.__dict__['printall']()
