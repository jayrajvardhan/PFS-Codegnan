'''
Polymorphism:
-------------
--> This means many forms it allows the same function, method, or operator to
behave differently depending on the object..

1.method overloading:
--------------------
--> method overloading means defining multiple methods with the same name but
different parameters.
eg-1:
--
class cal:
    def add(self,a,b,c=0):
        return a + b + c
an = cal()
print(an.add(20,10))
print(an.add(10,20,30))

eg-2:
----
class cal:
    def add(self,a,b):
        return a + b 
    def add(self,a,b,c):
        return a + b + c
an = cal()
print(an.add(20,10))
print(an.add(10,20,30))

2.method overriding:
-------------------
--> This occurs in a child class provides its own implementation of a method already
defined in the parent class.
eg-:by using super keyword
--
class Animal:
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
ob = dog()
ob.sound()
eg-2:
----
class Animal:
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
ob = dog()
ob.sound()

3.operator overloading:
----------------------
--> this operator overloading allows operators such as +,-,*,etc. To perform different
actions for user-defined objects.

note:
-----
--> this is the process of hiding internal implementation details and showing only the
essentials features to the user.
--> it focus on what an object does rather than how it does it..

eg:
--
class student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks
ob = student(4)
ob1 = student(78)
print(ob + ob1)


1.Method overloading:
--------------------
'''
class cal:
    def add(self,a,b,c=0):
        return a + b + c
an = cal()
print(an.add(20,10))
print(an.add(10,20,30))


'''
class cal:
    def add(self,a,b):
        return a + b 
    def add(self,a,b,c=0):
        return a + b + c
an = cal()
print(an.add(20,10))
print(an.add(10,20,30))
'''
'''
class cal:
    def add(self,*num):
        return sum(num) 
    def add(self,*num):
        return sum(num)
an = cal()
print(an.add(20,10))
print(an.add(10,20,30))
'''

class Animal:
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
ob = dog()
ob.sound()


class student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks

ob = student(4)
ob1 = student(78)
print(ob + ob1)


from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car started")

ob = car()
ob.start()




from abc import ABC, abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class rec(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return 2*(self.a * self.b)

ob = rec(10,5)
print(ob.area())
        

