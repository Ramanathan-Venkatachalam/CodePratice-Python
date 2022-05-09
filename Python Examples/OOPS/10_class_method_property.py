#Class Method Property

class member:
    count = 0 #ClassAttribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        member.count+=1

    def printDetail(self):
        print("Name=",self.name, "Age=",str(self.age))

    @classmethod
    #Creating a class method using decorator so that the python shall understand that its a class method
    #Common for all objects
    def total(cls):
        return cls.count

o = member("Rahul Dravid", 48)
o.printDetail()
print("Total member: ", member.total())
o1 = member("Sachin Tendulkar", 50)
o1.printDetail()
#The class method could be called using the class and object also
print("Total member: ", o1.total())
print("Total member: ", member.total())