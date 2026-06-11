'''
File handling:
--------------
--> File handler is an object of file to maintain several function of file like
creating, reading, updating and deleting file.

open a file:
------------
1.open()
2.with open()
modes:
-----
'r'--> it is used to reading the file, error if file does not exist
'a'--> it is used to add the txt file at last idex, if file does not exist
'w'--> it is used to add the txtx into file but it will override of all txt
inside the file. if the file file does not exist it will create
'x'--> used to create the file. But it will throws error if we are used to 'r'
mode to create.

methods:
-------
write()
read()
------
--> this method can read entire file line by line where we can specify the size
readline()
----------
--> it can read only one line at a time in a file.
eg:
--
s = open('demo.txt', 'r')
print(s.readline())
s.close()
readlines():
-----------
--> it will read entire file and gives in a list where each line is each index
in the list.
'''
s = open('demo.txt', 'r')
print(s.read())
s.close()

with open('dem.txt', 'w') as s:
    print(s.write('python'))


with open('sample.txt', 'w') as so:
    so.write('Hello welcome to python class')

with open('sample.txt', 'a') as so:
    so.write('\nToday we are learning basics of python programming')

'''
s = open('demo.txt', 'r')
print(s.read())
s.close()
'''
with open('demo.txt', 'r') as so:
    print(so.read(2))

'''
s = open('demo.txt', 'r')
print(s.readlines())
s.close()
'''
import os
os.remove('dem.txt')


