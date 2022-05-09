class Student:
    #Attributes/Variables of Class
    name = 'Rahul Dravid'
    age = 48

#To access or get the class attribute there are different ways
#1. getattr (inbuild function)
#Syntax = getattr(ClassName, 'VariableName', 'Optional')
print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
print(getattr(Student,'gender', 'No Such Variable'))

#2. Dot notation (frequently used)
#Syntax = ClassName.VariableName
print(Student.name)
print(Student.age)

#To update or set the class attribute there are again two different ways
#1. setattr (inbuild function)
#Syntax = setattr(ClassName, 'VariableName', 'VariableValue')
setattr(Student, 'name', 'Sachin Tendulkar')
print(Student.name)

#2. Dot notation (frequently used)
#Syntax = ClassName.VariableName = 'VariableValue'
(Student.gender) = "Male"
print(Student.gender)
print(Student.__dict__)

#To delete or remove the class attribute there are again two different ways
#1. delattr (inbuild function)
#Syntax = delattr(ClassName, 'VariableName')
delattr(Student, 'gender')
#To verify whether the variable/attributes is deleted we shall use the inbuild __dict__ function
print(Student.__dict__)

#2. Dot notation (frequently used)
#Syntax = del ClassName.VariableName
del (Student.age)
print(Student.__dict__)
