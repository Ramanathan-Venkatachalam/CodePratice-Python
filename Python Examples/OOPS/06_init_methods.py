# init method in Python (Constructor)
#When you create a new instance every time by default the __init__ method will be called
#It is used to assign or intialize values

class user:
    def __init__(self,name):
        print('Call when the new instance created')
        self.name = name
    def printall(self):
        print('Name= ', self.name)

obj1 = user('Sachin Tendulkar') #Creating a instance, instance attribute
obj1.printall()
print(obj1.__dict__) #The instance attribute 'name' will be only present in the instance dictionary

obj2 = user('Rahul Dravid') #Instance attribute, instance attribute
print(obj2.__dict__) #The instance attribute 'name' will be only present in the instance dictionary
print(user.__dict__) #The instance attribute 'name' will be not be present in the class dictionary
