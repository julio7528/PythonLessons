#Struc Example using Class
    #Define Class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

employee1 = Employee("John", 25, 10000)

    #Accessing Class Attributes
print(employee1.name)
print(employee1.age)
print(employee1.salary)

    #Manipulate Class Attributes
employee1.name = "Jack"
print(employee1.name)



#Struc Example using NamedTuple
# from collections import namedtuple
# Employee = namedtuple("Employee", ["name", age, salary])
# employee1 = Employee("John", 25, 10000)

