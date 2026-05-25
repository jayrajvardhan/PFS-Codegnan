'''
assert:
-------
--> this is debugging statement, which is used to test whether a condtion true or not.

eg:

n = 10
assert n > 15
print("True")

assert error:
-------------
n = 10
assert n > 15
print("True")

functions :
-----------
--> the function is a block of code which only executes when it is called.
--> we can pass data known as parameters into a function
--> To avoid repeated lines in code

eg : def function_name(parameters):
        -----------
        -----------
     function_name(arguments)

eg :

n = 9
def even(n):
    print(n)
even(n)


n = 9
def even(n):
    if n % 2 == 0:
        print(f"{n} Even")
    else:
        print(f"{n} Odd")
even(n)
even(109)

key to pass arguments:
----------------------
1.required arguments
--------------------
--> A function must be called with the same number of arguments.
eg :

def even(n,n2):
    if n % 2 == 0:
        print(f"{n} Even")
    else:
        print(f"{n} Odd")

even(109,90)

2. Default arguments:
---------------------
--> by default values is defined at parameters even though it will take from arguments.
eg :

def even(name = "jay", course = "python full stack", branch = "vizag"):
    print(name)
    print(course)
    print(branch)
even("jayraj", "Java full stack", "Hyderabad")


keyword length arguments:
-------------------------
--> we can say arguments with key = value syntax. By this, the order of arguments does not matter..

eg:
def even(name,course,branch):
    print(name)
    print(course)
    print(branch)
even("jayraj", "Java full stack", "Hyderabad")



'''


'''
'''

n = 10
assert n > 5
print("True")


n = 9
def even(n):
    print(n)
even(n)



def even(n,n2):
    if n % 2 == 0:
        print(f"{n} Even")
    else:
        print(f"{n} Odd")

even(109,90)



def even(name = "jay"):
    print(name)
even("jayraj")


def even(name = "jay", course = "python full stack", branch = "vizag"):
    print(name)
    print(course)
    print(branch)
even("jayraj", "Java full stack", "Hyderabad")


'''
def even(name,course,branch):
    print(name)
    print(course)
    print(branch)
even("jayraj", "Java full stack", "Hyderabad")
'''

'''
variable length arguments:
--------------------------
--> adding a star(*) before the parameter name in the function receives a tuple of arguments and
can access items with the indexes.

eg :

def even(*name):
    print(name[1])
even("jay", "chaitanya", "ramesh")


'''

'''
def even(*name):
    print(name[1])
even("jay", "chaitanya", "ramesh")
'''

name = "jay"
def even(any):
    print(any)
even(name)


