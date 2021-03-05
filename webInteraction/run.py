#!/usr/bin/env python3
import os
import requests
import sys
import json
from threading import Thread

def extract_data(in_file):
    """Open file and extract data according to its line"""
    with open(in_file,"r") as feedback:
        feedback_list=feedback.readlines()
    feedback_dict={}
    feedback_title=["title","name","date","feedback"]
    #Iterate through each line of the file and add them to the dictionary with coresponding keys
    for title,content in zip(feedback_title,feedback_list):
        feedback_dict[title]=content.strip()
    return feedback_dict


def upload_data (in_file,url):
    """Upload extracted data from a file to web server"""
    #Add information to key:value pairs dictionary
    feedback_data=extract_data(in_file)

    #Send request to the server with the extracted information
    response=requests.post(url,json=feedback_data)
    
    #Message the user if the information uploaded successfully or not
    if response.status_code==201:
        print("[+] {} uploaded successfully to server".format(in_file))
    else:
        print("[-] {} failed to upload to server! Status code: {}".format(in_file,response.status_code))


def process_data(in_dir,url):
    """Iterate through the directory to process file then upload the information to the web server"""
    #Check if the entered directory exist or is a directory 
    if not os.path.exists(in_dir):
        print("[-] {} does not exist!".format(in_dir))
        sys.exit(1)
    elif not os.path.isdir(in_dir):
        print("[-] {} is not a directory".format(in_dir))
        sys.exit(1)
    #Use os.walk to go through the directory and extract information from each file
    for root,_,files in os.walk(in_dir):
        for feedback in files:
            path=os.path.join(root,feedback)

            #Start upload threading for each file in the directory
            t=Thread(target=upload_data, args=(path,url))
            t.start()
            t.join()
    print("[+] Reaching end of directory")
            

#Change 34.71.23.11 to the IP of your web server
process_data("/data/feedback/","http://34.71.23.11/feedback/")
