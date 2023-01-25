# Description: Nested dictionary using a dictionary as a value
outerDict = {
    'x':5, 
    'InnerDict':{
        'y':10,
        'z':15
    }
}

print(outerDict['InnerDict']['z'])

# Description: Nested Structure using Class
class Inner:
    def __init__(self, y, z):
        self.y = y
        self.z = z

class Outer:
    def __init__(self, x, inner):
        self.x = x
        self.inner = inner

inner = Inner(10, 3.14)
outer = Outer(5, inner)

print(outer.inner.z)

#Array Structs using Python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(1, 2)
print(p.x)
print(p.y)

#NamedTuples using Fields
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x)
print(p.y)