'''
Regualr expression(RegEx):
-------------------------
--> RegEx is a sequence of characters that form a searching pattern.
--> this can be used to check if a string contain the specified search pattern.
--> python has a built-in package called 're' which can be used to work
with RegEx..

functions in re:
---------------
1.Findall
2.search
3.fullmatch

Metachar:
--------
[]--> a-z, A-Z, 0-9 and any specified sequence.
. --> here each dot is one char
^ --> this look for the string is starting with specified sequence or not.
$ --> this look for the string is ending with specified sequence or not.
* --> zero or more
? --> zero or one
+ --> one or more
{} --> 
'''
import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.findall('[a]', so))

import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.search('[als]', so))

import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.findall('[a-z]', so))

import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.findall('py.h.n', so))

import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.search('py.h.n', so))

import re
so = "My name is jay iam currently learning python full stack at codegnan"
print(re.findall('^My', so))

import re
so = "mahesh babu is a versatile actor in film industry"
print(re.findall('industry$', so))

import re
so = "mahesh babu is a versatile actor in film industry"
print(re.findall('m.*', so))

import re
so = "python is a foundational"
print(re.findall('p.*thon', so))

import re
so = "python is a foundational"
print(re.findall('p.?thon', so))

import re
so = "python is a foundational"
print(re.findall('p.{7}', so))

import re
so = "python is a foundational"
print(re.findall('p.*n', so))

'''
special sequence
----------------
\S --> No space
\s --> only space
\D --> non-digit
\d --> only digits
\w --> matches any word char(letters, digits, underscore)
\W --> non-words
'''
import re
so = "python is a foundational"
print(re.findall('\S', so))

import re
so = "python is a foundational"
print(re.findall('\s', so))

import re
so = "python is a 567 foundational"
print(re.findall('\d', so))

import re
so = "python is a 567 @foundational"
print(re.findall('\W', so))

'''
fullmatch
---------
'''
import re
mob = input("enter 10 digit mobile number: ")
any = re.fullmatch('[6-9][0-9]{9}', mob)
if any:
    print(f"{mob} this is india number")
else:
    print(f"{mob} this is not india number")
