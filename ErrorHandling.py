'''
Error Handling:
--------------
try block:
---------
--> the try block, test a block of code of error
eg:
--
try:
    print(a)
except:
    print("Hi")

Except block:
------------
--> the except block let hand if the code contain errors..
eg:
--
try:
    print(10/10)
except:
    print("This will handle ZeroDivisionError")

else block:
----------
--> this will be executed, if the try block has no errors in the code..
eg:
--
try:
    print(a)
    print(12+"jayraj")
except NameError:
    print("This will handle NameError")
except TypeError:
    print("This will handle TypeError")
else:
    print("No Error")




finally block:
-------------
--> this will be executed either try block contain error or not
'''

'''
try:
    print(a)
except:
    print("Hi")

'''

'''
try:
    print(10/10)
    print(a)
except:
    print("This will handle ZeroDivisionError")
'''
'''

try:
    print(5+"Py")
except NameError:
    print("This will handle NameError")
else:
    print("No error")
'''

# it will only handle the handle on the flow of try block
'''
try:
    print(a)
    print(12+"jayraj")
except NameError:
    print("This will handle NameError")
except TypeError:
    print("This will handle TypeError")
else:
    print("No Error")
'''

'''
try:
    print(12+"jayraj")
    print(a)
except NameError:
    print("This will handle NameError")
except TypeError:
    print("This will handle TypeError")
else:
    print("No Error")
finally:
    print("finally block")

'''

try:
    print("Hai")
except:
    print("Error")
else:
    print("no error")
finally:
    print("The End")


a = 5
try:
    print("hello")
except:
    print("error")
else:
    print("no error")
finally:
    print("the end")
    

try:
    print(12+"jayraj")
    print(a)
except NameError:
    print("This will handle NameError")
except TypeError:
    print("This will handle TypeError")
else:
    print("No Error")
finally:
    print("finally block")


