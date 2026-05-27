'''
num = 0
num2 = 1
def finaaci(num,num2):
    limit = int(input("Enter the limit: "))
    print(num,num2,end=" ")
    for i in range(1,limit):
        num3 = num + num2
        num = num2
        num2 = num3
        print(num3, end=" ")
finaaci(num,num2)
'''

any = [2,5,7,9,2,7]
empty = []
def dup(any,empty):
    for j in any:
        if j not in empty:
            empty.append(j)
    print(empty)
dup(any,empty)


any = "Welcome to the python programming".split()
def word_str(any):
    print(any)
word_str(any)


count = 0
any = "Welcome to the python programming".split()
def word_str(any,count):
    for j in any:
        count += 1
    print(count)
word_str(any,count)
            
