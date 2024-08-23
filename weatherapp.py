import smtplib

import requests as r

import time

import os

from dotenv import load_dotenv

load_dotenv()

def SendEmail():
    
    '''This Function asks for the sender's email and the message to be sent and them mails it'''
    
    l = [] # * Enter the email ids of the people you want to send an email to
    
    m = "It's raining!!!"
    

    sender = os.getenv('email')
    p = os.getenv('key')

    # * creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # * start TLS for security
    s.starttls()

    # * Authentication
    s.login(sender, p)

    for i in l:
        # * sending the mail
        s.sendmail(sender, i, m)

    # * terminating the session
    s.quit()

flag = True

latitude = os.getenv('latitude') # * change this to your desired latitude

longtitude = os.getenv('longtitude') # * change this to your desired longtitude

a = 'https://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longtitude+'&appid='+os.getenv('api')+'&units=metric'

while True:

    response = r.get(a)

    info = response.json()['weather'][0]['main']

    print(info)


    if flag:
        if info.lower() in ['rain','rainy','raining']:
        
            SendEmail()
        
            flag=False

    # * This is for sending the email every minute while it's raining
    # * The best case would be tell us when the rain starts and not keep repeating that while it's still raining

    if flag==False:
        
        if info.lower() not in ['rain','rainy','raining']:
        
            flag = True

    time.sleep(60)

