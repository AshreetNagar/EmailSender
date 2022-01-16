import pandas as p
from datetime import datetime as dt
import random as r
import smtplib

now = dt.now()
today = (now.month, now.day)

my_email = "lishantharmasothy@gmail.com"
password = "@Ghostassassin1"

skim = p.read_csv('birthdays.csv')
birthdaydict = {(row['month'], row['day']): row for (index, row) in skim.iterrows()}

if today in birthdaydict:
    path = f'LetterTemplates\letter_{r.randint(1,3)}.txt' 
    with open(path) as letter:
        person = birthdaydict[today]
        newLetter = letter.read()
        letter = newLetter.replace('[NAME]', person['name'])

with smtplib.SMTP('smtp.gmail.com') as send:
    send.starttls()
    send.login(user=my_email, password=password)
    send.sendmail(from_addr=my_email, to_addrs=person['email'], msg=f"Subject: Happy Birthday!\n\n{letter}")