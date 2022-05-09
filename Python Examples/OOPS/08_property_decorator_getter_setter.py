#Property Decorator Getter Setter

class players:
    def __init__(self, total):
        self._total = total #privatevariable

    def average(self):
        return self._total / 5.0

    #To access the private variable write a getter function
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        #ValidationProcess
        if t<0 or t>500:
            print('Value cannot be changed')
        else:
            self._total = t

obj = players(450)
print('Total= ',obj.total)
print('Average= ',obj.average())

obj.total = 550
print('Total= ',obj.total)
print('Average= ',obj.average())