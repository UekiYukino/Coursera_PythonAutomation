#!/usr/bin/env python3

import reports 
import os
import datetime
import emails
import time

def process_time():
    """Get current datetime and return in format
    Eg: March 10,2021"""
    current=datetime.datetime.now()
    return current.strftime("%B %d, %Y")


def extract_data(in_file):
    """Extract the data from description file for the report"""
    with open(in_file) as data:
        lines=data.readlines()
        #Extract the name and weight then add them to the paragraph
        name=lines[0].strip()
        weight=lines[1].strip()
        data_paragraph="name: {}<br/>weight: {}<br/><br/>".format(name,weight)
        return data_paragraph


def process_data(in_dir):
    """Process all the description files within a directory and generate a paragraph from them"""
    paragraph=""
    #Check if the path entered exist or not
    if not os.path.exists(in_dir):
        print("[-] {} does not exist".format(in_dir))

    #Process the directory and try to extract the data, ignore if the file is invalid
    for in_file in os.listdir(in_dir):
        file_path=os.path.join(in_dir,in_file)
        try:
            paragraph+=extract_data(file_path)
        except:
            continue
    return paragraph



def main():
    """The main function, generate report to be sent through email"""
    #Call the process_time() function to retrieve the current time in readable format
    current=process_time()
    title="Processed Update on {}".format(current)
    #supplier-data/description is the path to the directory which stored the description files
    paragraph=process_data("supplier-data/descriptions")
    reports.generate_report("/tmp/processed.pdf",title,paragraph)

    #Add information to the email and send it
    sender="automation@example.com"
    recipient="{}@example.com".format(os.environ.get("USER"))
    subject= "Upload Completed - Online Fruit Store"
    body= "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    attachment="/tmp/processed.pdf"
    
    message=emails.process_email(sender,recipient,subject,body, attachment)
    emails.send(message)
    

if __name__ == "__main__":
    main()
