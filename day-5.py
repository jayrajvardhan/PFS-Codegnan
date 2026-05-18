'''
sets
-----
-> A set is a collection of unique and unordered elements.
-> it is unordered.
-> Duplicate values are not allowed.
-> items are not stored in index order.
-> represented in {}

methods
--------
-> union():it will give all the values or elements from two sets together in once
   syntax : variable_name.union(another var)

-> intersection():to get the common elements from both sides.
   syntax : variable_name.intersection(another var)

-> difference(): it is used to get the different values from the set
   syntax : vairable_name.difference(another var)

-> symmetric_difference(): it is used to get the elements which are not common
   syntax : variable_name.symmetric_difference(another var)

-> add(): to add new elements into set.
   syntax : variable_name.add(element)

-> update() : it is used to add multiple items into set
   syntax : variable_name.update([elements])

-------------

--> 
'''

a = [1,2,2,3,4]
print(a)

a = {1,2,3,4}
n ={34,56,78}
print(a)
print(a | n)
print(a.union(n))


a = {1,2,3,4}
n ={2,3}
print(a)
print(a & n)
print(a.intersection(n))


a = {1,2,3,4}
n ={2,3,56,78,99}
print(a)
print(a and n)
print(a.intersection(n))




a = {1,2,3,4}
n ={2,3,56,78,99}
print(a)
print(a - n)
print(a.difference(n))


a = {1,2,3,4,5}
n = {2,3,4,78,99}
print(a)
print(a ^ n)
print(a.symmetric_difference(a))


a = {1,2,3,4,5}
a.add(6)
print(a)

a = {1,2,3,4}
a.update([25,78])
print(a)

a = {1,2,3,4}
print(sum(a))


a = {1,2,3,4}
print(max(a))

a = {1,2,3,4}
print(min(a))


a = {1,2,3,4}
a.remove(2)
print(a)







