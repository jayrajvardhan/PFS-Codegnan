'''
Inheritance:
------------
--> This intheritance allows one class to acquire the properties and methods of another class.
Types:
-----
1.Simple inheritance:
---------------------
-->A class inhert from a single parent class is called single inheritance.
eg:
--
class father:
    def Land(self):
        print("I am father have 5A")

class jay(father):
    def my_own(self):
        print("i have 2A")

fam = jay()

fam.Land()

2.Multiple inheritance:
-----------------------
-->A child class inherited from more than one parent class that is called multiple inheritance.
eg:
--
class father:
    def Land(self):
        print("My father have 5A")
class mother:
    def gold(self):
        print("my mother have 1kg of gold")

class jay(father,mother):
    def my_own(self):
        print("i have nothing")

all = jay()
all.Land()
all.gold()

3.Multi-level inheritance:
--------------------------
-->A class inherits from a parent class and another class inherits from that child class.
eg:
--
class grandfather:
    def land(self):
        print("My grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print("have flat at hyderabad")
class son(father):
    def ntg(self):
        print("I have both properties")

ob = son()
ob.land()
ob.flat()
ob.ntg()

4.Hierarchical inheritance:
---------------------------
--> Multiple child classes inherit from a single parent..
eg:
--
class father:
    def land(self):
        print("my father has 10A of land")
class jay(father):
    def mine(self):
        print("working")
class raja(father):
    def bro(self):
        print("studying")

a = raja()
a.land()
b = jay()
b.land()

5.Hybrid inheritance:
----------------------
--> The combination of two or more types of inheritance 
'''
'''
class father:
    def Land(self):
        print("I am father have 5A")

class jay(father):
    def my_own(self):
        print("i have 2A")

fam = jay()

fam.Land()
'''

'''
class father:
    def Land(self):
        print("My father have 5A")
class mother:
    def gold(self):
        print("my mother have 1kg of gold")

class jay(father,mother):
    def my_own(self):
        print("i have nothing")

all = jay()
all.Land()
all.gold()
'''

'''
class grandfather:
    def land(self):
        print("My grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print("have flat at hyderabad")
class son(father):
    def ntg(self):
        print("I have both properties")

ob = son()
ob.land()
ob.flat()
ob.ntg()
'''

class father:
    def land(self):
        print("my father has 10A of land")
class jay(father):
    def mine(self):
        print("working")
class raja(father):
    def bro(self):
        print("studying")

a = raja()
a.land()
b = jay()
b.land()


class A:
    def some(self):
        print('Class A')
class B(A):
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')
class D(B,C):
    def All(self):
        print('Class D')
ob = D()
ob.so()
'''
Super() method:
--------------
--> Super() is used to access methods and constructor of the parent class from the child class.
eg:
--
class parent:
    def display(self):
        print('Method parent')
class child(parent):
    def display(self):
        super().display()
        print('Method child')

any = child()
any.display()

'''
class parent:
    def display(self):
        print('Method parent')
class child(parent):
    def display(self):
        super().display()
        print('Method child')

any = child()
any.display()
'''
how to access attributes directly:
---------------------------------
'''
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")
        
any = student('jay', 120)
any.show()
    
