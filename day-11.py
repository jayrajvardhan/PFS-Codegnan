'''
built-in functions:
-------------------
print(): to see the output of the particular variable.
input():
len(): to find out the length of the variable
eg : string, list
type():
max():
min():
sort(): it will permenently sorts the value.
sorted() : it will sort only at run time.
return() : it holds the values. it does not shows the values.

recursive functions
-------------------
--> A recursive function that calss itself to solve a problem by breaking into small or simple
sub-problem.
'''
m = [3,4,1,2]
m.sort()
print(m)

'''
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)
print(fac(5))
'''

'''
def even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
even(7)
'''

'''
return : this ends a function execution and sends a value back to the code that
called the function.

eg:

def add(a,b):
    return a + b
res = add(3,5)
print(res)
'''

'''
lambda functions
----------------
--> it is also called as single line function
--> A lambda function can take n number of arguments but only one expression.
synatx:
lambda arguments : expression

'''
so = lambda a,b,c: a+b+c+a
print(so(7,9,6))

'''

any = lambda a,b: a+b
so = any(4,5)
print(so)
print(any(6,9))
'''

so = lambda a,b: a-b
print(so(5,4))

so = lambda a,b: a*b
print(so(3,5))

so = lambda a,b: a/b
print(so(12,4))

so = lambda a,b: a^b
print(so(4,5))

so = lambda a: a**2
print(so(4))

so = lambda a,b: a%b
print(so(4,5))

