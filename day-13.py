'''
List comprehension:
-------------------
--> list comprehension offers a shortest syntax we want to createe a new list from
existing list
syntax
------>
variable_name = [expression loop condition]

old = [1,2,3,4,5]
new = [so for so in old if so%2==0]
print(new)

old = [1,2,3,4,5]
new = [so if so%2!=0 else "even" for so in old]
print(new)

GENERATORS:
------------
--> The generators in python are a special type of itterable, allowing users to iterate
over data efficiently without storing everything in the memory.
--> They generates the values lazily yield keyboard.

why to use gen
--------------
--> generators do not store the entire dataset in memory, they generate values
on the flyer runtime.
--> avoiding the unnecessary storage of data speedup execution.

how it works:
------------
--> it looks like normal function but uses the yield keyboard instead of return.
--> when the function is called, it does not execute immediately. instead it return a
generator object which can be iterated using loop or the next() function.

def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
'''

def any(num):
    for i in range(num):
        yield i * i
a = any(5)
print(next(a))
print(next(a))
print(next(a))


def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i * i)
    return result
print(sqr(10))


s = "My name is jayraj"
any = ""
for j in s:
    if j not in "AEIOUaeiou":
        any += j
print(any)
