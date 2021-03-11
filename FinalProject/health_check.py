#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails
from email.message import EmailMessage
import time

def over_cpu():
    """Checking if the CPU usage in a 1s interval is above 80% or not"""
    cpu_used=psutil.cpu_percent(1)
    return cpu_used>80

def low_disk():
    """Checking if the disk space available is lower than 20% or not"""
    du=shutil.disk_usage("/")
    percent_free=(du.free/du.total)*100
    return percent_free < 20

def not_localhost():
    """Check if the localhost name is 127.0.0.1 or not"""
    localhost=socket.gethostbyname("localhost")
    return localhost!="127.0.0.1"

def low_mem():
    """Check if the free memory is lower than 500MB or not"""
    #Get the current free memory space and convert from bytes -> MB
    free_mem=psutil.virtual_memory().free*9.537*(10**(-7))
    return round(free_mem,0) < 500

def main():
    """Check the system regularly and send email when error occured"""
    sender="automation@example.com"
    recipient="{}@example.com".format(os.environ.get("USER"))
    body= "Please check your system and resolve the issue as soon as possible."

    #Create the email
    message=EmailMessage()
    message["From"]=sender
    message["To"]=recipient
    message.set_content(body)
    
    #Run the program in the background and check for errors then call the send method from reports.py to send the emails
    while True:
        if over_cpu():
            message["Subject"]="Error - CPU usage is over 80%"
            emails.send(message)
        if low_disk():
            message["Subject"]="Error - Available disk space is less than 20%"
            emails.send(message)
        if low_mem():
            message["Subject"]="Error - Available memory is less than 500MB"
            emails.send(message)
        if not_localhost():
            message["Subject"]="Error - localhost cannot be resolved to 127.0.0.1"
            emails.send(message)
        #Wait 60 second before funning the test again
        time.sleep(60)

if __name__ == "__main__":
    main()
