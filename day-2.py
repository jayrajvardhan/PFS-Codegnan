print(4 % 5 == 0)
print(2 * 3)
print(10**2)
print(10/2)
print(35.20//5)


Count = 0
for j in range(1,10):
    Count += 1
    print(Count)


a = 7
b = 9
print(a == b)

a = [1,2]
b = [1,2]
c = a
print(type(a))
print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is not b)

'''---> Logical Operator:
and--> This operator is used to check Both should be true.
or--> This operator is used to check any one of the statement should be true
not-->
'''

''' 1)and:
a = 5
if a % 3 == 0 and a % 5 == 0:
     print("True")
'''

a = 15
if a % 3 == 0 and a % 5 == 0:
    print("True")


a = 5
if a % 3 == 0 or a % 5 == 0:
    print("True")

'''membership
a = 7
b = [1,2]
print(a not in b)
'''
'''
a = 7
b = [1,2]
print(a not in b)
'''
'''
print(5&3)
print(5|3)
'''

'''
any = "python78,&"
for j in any:
    print(j)
'''

'''methods
----------
replace()
'''

'''
any = "python is a language"
print(any.replace("python", "java"))
print(any)
'''

'''
any = "python is a language"
print(any.split())

any = "python is a language"
print(any.split("$"))
'''

'''
any = "My name is jay"
print(len(any))
'''

'''
any = "My name is jay"
print(any[3:10])
'''

'''
indexing : it is used to get substring present in that position..
'''

any = "python is a language"
print(any[7])
print(any.index("ang"))
