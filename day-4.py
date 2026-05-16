'''
Concatination :
---------------
--> the (+) for int and can add, but for other data types it will act as concatinating the data type or values

a = 90
b = 8
print(a+b)
any_ = "python "
st = "is a language"
print(any_ + st)
an = [1,2]
am = [3,4]
print(an + am)

tuple
-----
--> it is a collection of different data types and seperated by commas(,) and represented in paranthesis()
and tuple is immutable.
methods
-------
count()
-------
--> this is used to count the particular item in the tuple

syntax--> variable_name.count(item)

index()
-------
--> it is used to find out the index position of the item, and only gives the first occurance

'''
some = (1,"python",[1,2],(3,4))
print(some)
print(some[2][1])
print(some.count("python"))
print(some.index("python"))

any = (1,"python",(1,2,(34,"this is python 3rd class",78),"python is a language",89),34,(3,4))
print(any[2][2][1][8])

'''
Dictionary
-----------
-->it is a collection of key : value pair, key and value is seperated by : and pair is
seperated by comma
-->represented by {}
ex : syntax : dict.keys()
'''

jay_details = {"name" : "jay",
               1 : 2,
               (1,2) : [3,4]}
print(jay_details)
print(type(jay_details))

'''
methods
-------
1) keys() : it is used to retrieve all the keys of the dictionary.
syntax : dict.keys()
2) values() : it is used to retrieve all the values of the dictionary.
syntax : dict.values()
3) items() : it is used to get key and value together
syntax : dict.items()
4) update() : it is used to add a new key : value pair into dict
syntax : dict.update({key:value})
5) clear() : it is used to remove all the items in the dict


'''
jay_details = {"name" : "jay",
               "age"  : 21,
               "mobile" : "6305215264",
               "Aadhar" : "xxxxxxxxxx"}
print(jay_details)
print(jay_details.keys())


jay_details = {"name" : "jay",
               "age"  : 21,
               "mobile" : "6305215264",
               "Aadhar" : "xxxxxxxxxx"}
print(jay_details)
print(jay_details.values())


jay_details = {"name" : "jay",
               "age"  : 21,
               "mobile" : "6305215264",
               "Aadhar" : "xxxxxxxxxx"}
print(jay_details)
print(jay_details.items())



jay_details = {"name" : "jay",
               "age"  : 21,
               "mobile" : "6305215264"}
print(jay_details["name"])


jay_details = {"name" : "jay",
               "age" : 21,
               "Course" : "B.Tech",
               "Trainee" : "Python full stack"}
jay_details.update({"Name of the institute" : "codegnan"})
print(jay_details.items())
jay_details.clear()
print(jay_details)








