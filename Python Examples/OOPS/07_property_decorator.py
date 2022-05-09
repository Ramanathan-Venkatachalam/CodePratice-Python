#Property Decorator
#To update the instance attribute in the entire class we shall first covert that instance attribute as function and make them as property decorator

class players:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.msg = self.name + ' is ' + str(self.age) + ' years old'

    @property #Decorator
    def msg(self):
        return self.name + ' is ' + str(self.age) + ' years old'

o=players('Rahul Dravid', 48)
print(o.name)
print(o.age)
print(o.msg)
o.age=50 #Updating the instance attribute value
print(o.msg)
o.name="Sachin" #Updating the instance attribute value
print(o.msg)