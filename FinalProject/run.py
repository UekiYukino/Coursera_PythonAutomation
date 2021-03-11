#!/usr/bin/env python3
import os
import requests

def extract_data(in_file):
    """Extract data from description files then store them in a dictionart"""
    headers=["name","weight","description"]
    description_dict={}
    with open(in_file) as data:
        #Use readlines() method to stored lines data into a list
        lines=data.readlines()
        description_dict["name"]=lines[0].strip()
        
        #Extract the weight and convert it to int
        weight=lines[1].strip().replace(" lbs","")
        description_dict["weight"]=int(weight)
        
        description_dict["description"]=lines[2].strip()
    #Replace the txt extension with jpeg extension to retrieve the image file for the data description
    image_name=in_file.replace("txt","jpeg")
    #Use os.path.basename() method to extract the file name only
    description_dict["image_name"]=os.path.basename(image_name)
    return description_dict

def upload_data(in_file,url):
    """Upload the extracted information to the web server"""
    exdata=extract_data(in_file)
    response=requests.post(url, json=exdata)
    #Message the user if the upload is successfull or not
    if response.status_code == 201:
        print("[+] Data from {} uploaded successfully".format(in_file))
    else:
        print("[-] {} failed with status code {}".format(in_file,response.status_code))

def process_data(in_dir,url):
    """Walk through the directory and proceed to upload the files to server"""
    for in_file in os.listdir(in_dir):
        #Join filename with directory name to create file path
        file_path=os.path.join(in_dir,in_file)
        #Skip directory
        if not os.path.isdir(file_path):
            upload_data(file_path,url)

process_data("supplier-data/descriptions/","http://localhost/fruits/")
