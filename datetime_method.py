'''
Date and time:
--------------
--> python provides the built-in datetime module to work with data and time.

import datetime
---------------
'''
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)

'''
import datetime
today = datetime.date.today()
now = datetime.datetime.now
print(now)
print(today)
'''
import datetime
now = datetime.datetime.now()

print(f"Year is:{now.year}")
print(f"Month is:{now.month}")
print(f"Day is:{now.day}")
print(f"Hour is:{now.hour}")
print(f"Minute is:{now.minute}")
print(f"Second is:{now.second}")

'''
Formatting date and time:
-------------------------
--> strftime() is a method used to format date and time

%d--> day
%m--> month
%Y--> year
%H--> Hour
%M--> minutes
%S--> Seconds
eg:
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
'''
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

import datetime
date_1 = datetime.date(2025,6,1)
date_2 = datetime.date(2026,6,1)
differ_ = date_2 - date_1
print(differ_)

'''
timedelta:
---------
import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(future)
'''
import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)
print(future)

'''
ctime
-----
import datetime
day = datetime.date.today()
print(day.ctime())
'''

import calendar

today = datetime.date.today()
year = 2026
month = 7
print(calendar.calendar(year,month))


import calendar

today = datetime.date.today()
year = 2026
month = 7
print(calendar.month(year,month))


import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender_mail = "jayrajvardhanp@gmail.com"
password = "zwnf ynpz uhpe jgqi"
receiver_mail = "jamirakesh123@gmail.com"
target_time = "10:30"

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == target_time:
        msg = EmailMessage()
        msg["Subject"] = "Welcome to email"
        msg["From"] = "jayrajvardhanp@gmail.com"
        msg["To"] = "jamirakesh123@gmail.com"
        msg.set_content("Hello rakesh nice to meet you")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_mail, password)
            smtp.send_message(msg)

        print("Email sent successfully")
        break

    time.sleep(30)
