#Property Decorator Getter Setter

class players:
    def __init__(self, total):
        self._total = total #privatevariable

    def average(self):
        return self._total / 5.0

#Getter Setter Methods
    def getter(self):
        return self._total

    def setter(self, t):
        #ValidationProcess
        if t<0 or t>500:
            print('Value cannot be changed')
        else:
            self._total = t

#To access the private variable use property method
    total = property(getter, setter)

obj = players(450)
print('Total= ',obj.total)
print('Average= ',obj.average())

obj.total = 200
print('Total= ',obj.total)
print('Average= ',obj.average())