for i in range(1,10):
    for j in range(1,2):
        print(j)


'''
n = 9
for j in range(1,11):
    print(n, "x", j, "=", n*j)
'''

s = "python"
print(s[::-1])


s = "python"
for j in s:
    print(j)

'''
s = "python"
emptystr= ""
for j in s:
    emptystr=emptystr + j
    print(emptystr)
'''

'''


s = input("Enter a word: ")
emptystr = ""
for j in s:
    emptystr = j + emptystr
    print(emptystr)
if emptystr == s:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")
'''
'''
n = int(input())
armstro = 0
len_ = len(str(n))
for i in str(n):
    armstro += int(i) ** len_
if armstro == n:
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is not a armstrong number")


num = int(input())
per_no = 0
for i in range(1,num):
    if num%i==0:
        per_no+=i
        print(per_no)
if per_no==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")


num = int(input("Enter a number: "))
count = 0
for k in range(1,num+1):
    if num%k == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} not a prime number")



star = 5
for a in range(1,star+1):
    for b in range(1,a+1):
        print("*", end="")
    print()

'''
star = int(input())
for a in range(1,star+1):
    for b in range(a):
        print(chr(65+b), end=" ")
    print()
    

star = 5
count = 0
for a in range(1,star+1):
    for b in range(1,a+1):
        count += 1
        print(b,end="")
    print()



star = 5
count = 0
for a in range(star,0,-1):
    for b in range(a):
        count += 1
        print("*",end="")
    print()


star = 5
count = 0
for a in range(1,star+1):
    for b in range(a):
        count += 1
        print(chr(65+b),end="")
    print()


num = 5
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

