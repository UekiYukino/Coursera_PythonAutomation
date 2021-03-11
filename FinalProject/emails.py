#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib

def process_email(sender, recipient, subject, body, attachment):
    """Process email and with information and attach files"""
    message= EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    #Set the content for the body of the email
    message.set_content(body)
    
    #Try to guess the file type of the attachment to send through email
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split("/", 1)

    #Attach the file to the email
    with open(attachment, "rb") as item:
        message.add_attachment(item.read(), 
                maintype=mime_type, 
                subtype=mime_subtype,
                filename= os.path.basename(attachment))
    return message

def send(message):
    """Send the email to the local SMTP server."""
    mail_server= smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()


