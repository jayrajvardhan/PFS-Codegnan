any = "python is a language"
print(any[::-1])

'''
1.program to convert 24h clock into normal clock

'''

'''
time_ = input("enter 24h time:")
parts_ = time_.split(":")
hour_ =int(parts_[0])
min_ = int(parts_[1])
conver_ =hour_ - 12
print(f"{time_} is converted into {hour_ - 12}:{min_} pm")

'''

'''
List : it is a collection of different data types
----> it is represented in square brackets[] and seperated by commas(,).
----> list is a mutable data type.
----> we can add item.

->Immutable
------------
--> Could not able to modify on the particular variable, so it is called immutable.
--> ex : int, string.
->Mutable
----------
--> we can able to modigy the particular variable.
--> ex : list

methods
-------
append() : this method is used to add new item into list and it will add in the last index position.

syntax--> varible_name.append(item)

extend() : this method is used to add itterable into list, and it will in the last index position, each value or substring is each in index in the list.

syntax--> variable-name.extend(itterable)

any = [1,2,3]
any.append(6)
print(any)
any.append(20)
print(any)


'''


'''
any = [1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][4])
'''

any = [1,2,3,4]
any.append(6)
print(any)
any.append([20,89])
print(any)

st = " my name is jay "
print(st.replace("jay", "jayraj"))
print(st)
list = [1,2,3,4]
list.append(6)
print(list)

'''
extend:
'''

any = [1,2,3,4,5]
any.append("python")
any.extend("python")
print(any)

'''
pop() : it is used to remove the item from the list, but will mention here index position in the pop method.

syntax: varibale_name.pop(index position)

remove() : it is used to remove the item from the list, but will mention here direct in the remove method.

syntax : varibale_name.remove()

'''
list = [1,2,3,4,5,6]
list.pop()
print(list)


str = ["python", 90 , "Java"]
str.remove("python")
print(str)






