'''
stu_marks = int(input('Enter the marks: '))
if stu_marks >= 90:
    print('A+')
elif stu_marks >= 80:
    print('A')
elif stu_marks >= 70:
    print('B+')
elif stu_marks >= 60:
    print('B')
elif stu_marks >= 50:
    print('C+')
elif stu_marks >= 35:
    print('Pass')
else:
    print('Fail')

'''

'''
a = int(input())
b = int(input())
c = int(input())
if a>b and b>c:
    print(a)
elif b>c and c>a:
    print(b)
else:
    print(c)

'''

'''
SBI_Bank = {'ATM PIN': '6600'}
pin = input('Enter 4 digit ATM pin: ')
if len(pin) == 4:
    if pin in SBI_Bank['ATM PIN']:
        print('Welcome to SBI ATM')
    else:
        print('INVALID PIN')
else:
    print('please enter 4 digit pin')

'''
'''
for stattement :
-----------------
--> it is used to iterate over a sequence.
ex: str = 'python'
lst = [1,2,3,4]
so = (5,6,7,8)
for j in str:
    print(j)
range() :
--------
--> range() is a in-built function used to generate numbers in sequential manner.
Synatx : range(start,end,step)

else in for:
-----------
--> once the iterations completed this else will be executed.
ex : 
for i in range(1,10):
    print(i)
else:
    print('code ended here')

break:
-----
--> it is used to exit from the loop based on the condition.

continue:
---------
--> it is used to skip the current itteration based on the condition.

pass:
-----
--> it is a space holder
'''


str = 'python'
lst = [1,2,3,4]
so = (5,6,7,8)
for j in str:
    print(j)

for i in range(1,10,2):
    print(i)



'''
for i in range(1,10):
    print(i)
else:
    print('code ended here')
'''

for i in range(1,10):
    print(i)
    if i == 5:
        continue
    print(i)

'''
while : it is the combination of for and if statement.
ex :
i = 1
while i > 5:
    print(i)
    i += 1
-------
'''

i = 1
while i > 5:
    print(i)
    i += 1
