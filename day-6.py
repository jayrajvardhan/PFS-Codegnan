'''
type conversions
----------------
the process of changing one data type to another data type but we can covert int
into string but we cannot convert string into int unless that string holds number.

'''
'''
int-->


a = 78
b = str(a)
c = float(a)
print(c)
print(type(c))
print(type(b))

'''

'''
str->

a = "10"
b = int(a)
print(type(b))

'''

"""a = "10"
b = int(a)
print(type(b))

a = "90"
b = float(a)
print(b)
print(type(b))
c = tuple(a)
print(c)


car = 90.78
print(int(car))
print(type(str(car)))

any = [7,8]
print(str(any))
print(tuple(any))

any = (8,9)
print(str(any))
print(list(any))

n = int(input("Enter a number:"))
print(85 + n)"""

'''
str = input("Enter a letter: ")
print(str)
'''

'''
any = list(map(int, input("Enter numbers: ").split()))
print(any)
'''

'''
any = tuple(map(int, input("Enter numbers: ").split()))
print(any)
'''
num = eval(input("Enter: "))
print(type(num))



