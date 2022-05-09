#Multiple Inheritance

class father:
    def trading(self):
        print('Trading Stocks')
    def chess(self):
        print('Playing chess from father')

class mother:
    def cooking(self):
        print('Cooking food')
    def chess(self):
        print('Playing chess from mother')

#DerivedClass
class son(father, mother):
    def ride(self):
        print('Riding Bicycle')

o = son()
o.ride()
o.trading()
o.cooking()
o.chess()