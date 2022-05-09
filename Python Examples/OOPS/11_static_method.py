#Static Method in Python

class member:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def printDetail(self):
        print('Name: ', self.name, "Age: ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to the Club")

m1 = member("Rahul", 45)
m1.printDetail()
m1.welcome()

m2 = member("Sachin", 50)
m2.printDetail()
m2.welcome()