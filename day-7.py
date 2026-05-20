'''
condition statement
-------------------
-> if : to check the statement is true or not.

-> if else : else in if statement, incase the condtiton becomes false then it will enter into flow-back(else),
   it will execute whatever inside it.
   eg :
n = int(input("Enter a number: "))
if n % 2 != 0:
        print(f"{n} is a odd number")
else:
        print(f"{n} is a even number")

-> nested if
-> elif:
'''

'''
n = 6
if n%2 == 0:
    print("Even")
else:
    print("Odd")


n = int(input("Enter a number: "))
if n % 2 != 0:
        print(f"{n} is a odd number")
else:
        print(f"{n} is a even number")
'''


age = 14
if age < 18:
    print("you have to wait for 3 years")
elif age > 18:
    print("you are eligible to vote")

'''
age = 11
if age > 18:
    print("you are eligible to vote")
else:
    print(f"you have to wait for {18-age} more years")
'''

n1 = 8
n2 = 5
if n1 >= n2:
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n2} is greater than {n1}")




year = 2026
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


vowel = 'a'
if vowel in 'AEIOUaeiou':
    print(f'{vowel} is a vowel')
else:
    print(f'{vowel} is a consonent')



n = 9
if n >= 0:
    print(f'{n} is a postitive number')
else:
    print(f'{n} is a negative number')


'''
marks = int(input("Enter the marks: "))
stu_name = input("Enter the student name: ")
if marks >=45:
    print(f"{stu_name} is passed in the exam")
else:
    print(f"{stu_name} is failed in the exam")
'''

'''
divisibility checking
---------------------
'''
n = 70
if n % 3 == 0 and n % 5 == 0:
    print(f'{n} is divisible by 3 and 5')
else:
    print(f'{n} is not divisible by 3 and 5')


num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")


str = input("Enter a letter: ")
if str in "AEIOUaeiou":
    print(f"{str} is a vowel")
else:
    print(f"{str} is a consonant")





