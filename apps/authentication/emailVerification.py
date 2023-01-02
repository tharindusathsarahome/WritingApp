import os
import math
import random
import smtplib
from apps import config


digits = "0123456789"
OTP_LIST = {}

def email_send(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(config.Config.EMAIL_ID,config.Config.EMAIL_APP_PASSWORD)
    s.sendmail('&&&&&&','ishan2017kanchana@gmail.com',message)
    return True

def email_use_send(emailid,message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(config.Config.EMAIL_ID,config.Config.EMAIL_APP_PASSWORD)
    s.sendmail('&&&&&&',emailid,message)


def email_otp_send(emailid):
    OTP = ""
    X=0
    for i in range (6):
        OTP += digits[math.floor(random.random()*10)]
    otp =  f"""Subject: Verify Your Email \n\nHi there,\n\nYou recently signed up for our AI content creation service, and we're excited to have you on board!\n\nIn order to get started, we just need to verify your email address. Please enter the code below into the verification page on our website.\n\nYour verification code is: {OTP}\n\nThank you, and we'll see you soon!\n\nAI Content Creation"""
    OTP_LIST[X] = OTP
    X+=1
    message = otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(config.Config.EMAIL_ID,config.Config.EMAIL_APP_PASSWORD)
    s.sendmail('&&&&&&',emailid,message)
    
def email_otp_verify(a): 
    for x in OTP_LIST :    
        if OTP_LIST[x] == a:
            return True
        else:
            return False