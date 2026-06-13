'''
Project based on RegEx:
-----------------------
validation
----------

1.Mobile number
----------------
rules

> 10 digit number
------------------

2.password:
------------
>captital, small, digit, special character, atleast 8

------------------

3. gmail
--------
> @gmail.com
'''

'''
import re
mob = input("Enter a mobile number: ")
if re.fullmatch(r'^[6-9][0-9]{9}',mob):
    print("valid number")
else:
    print("Invalid number")
'''
'''
import re
class MobileValidation:
    def Validation(self):
        mob = input("Enter 10 digit mobile number: ")
        pattern = re.fullmatch(r"[6-9][0-9]{9}", mob)
        if pattern:
            print(f"it is Valid mobile number")
        else:
            print(f"it is invalid mobile number")
ob = MobileValidation()
ob.Validation()

'''
'''
'''
import re
class UserValidation:
    def validate(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile Number: ")
        password = input("Enter Password: ")
        name_pattern = re.fullmatch(r"[A-Za-z ]{3,}", name)
        email_pattern = re.fullmatch(r"[a-zA-Z0-9._]+@gmail\.com", email)
        mobile_pattern = re.fullmatch(r"[6-9][0-9]{9}", mobile)
        password_pattern = re.fullmatch(r"(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[@#$%^&*!]).{8,}",password)
        if name_pattern:
            print(" Valid Name")
        else:
            print(" Invalid Name")

        if email_pattern:
            print(" Valid Email")
        else:
            print(" Invalid Email")

        if mobile_pattern:
            print(" Valid Mobile Number")
        else:
            print(" Invalid Mobile Number")

        if password_pattern:
            print(" Valid Password")
        else:
            print("Invalid Password")
obj = UserValidation()
obj.validate()



