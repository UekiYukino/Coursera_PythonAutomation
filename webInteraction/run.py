#!/usr/bin/env python3
import os
import requests
import json

def extract_data(in_file):
    with open(in_file,"r") as feedback:
        feedback_list=feedback.readlines()
    feedback_dict={}
    feedback_title=["title","name","date","feedback"]
    #Iterate through each line of the file and add them to the dictionary with coresponding keys
    for title,content in zip(feedback_title,feedback_list):
        feedback_dict[title]=content.strip()
    return feedback_dict

def process_data(in_dir,url):
    #Use os.walk to go through the directory and extract information from each file
    for root,_,files in os.walk(in_dir):
        for feedback in files:
            path=os.path.join(root,feedback)
            #Add information to a key:value pairs dictionary
            feedback_dict=extract_data(path)
            
            #Make post request to the server with the extracted information
            response=requests.post(url,json=feedback_dict)
            
            #Message the user if the file is uploaded successfully or not
            if response.status_code == 201:
                print("[+] {} uploaded successfully to server".format(path))
            else:
                print("[-] {} failed to upload to server with code {}".format(path,response.status_code))
    
#Change 35.232.200.181 to the IP of your web server
process_data("/data/feedback/","http://35.232.200.181/feedback/")
