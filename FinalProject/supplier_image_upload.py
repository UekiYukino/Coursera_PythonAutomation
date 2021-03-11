#!/usr/bin/env python3

import requests
import os
from threading import Thread

def upload_file (url,image_file):
    """Upload an image to a server using its URL"""
    #Open and read the image as binary then upload it using POST method
    with open(image_file, "rb") as file_upload:
        response= requests.post(url,files={"file":file_upload})
        if response.status_code==201:
            print("{} uploaded successfully".format(image_file))
        else:
            print("{} failed with status code {}".format(image_file,response.status_code))


def dir_upload (url, in_dir):
    """Walk though a directory then upload all .jpeg image files to the server"""
    for ifile in os.listdir(in_dir):
        #Upload .jpeg files only
        if ".jpeg" in ifile:
            file_path=os.path.join(in_dir,ifile)
            #Start uploading images using threading
            t=Thread(target=upload_file, args=(url,file_path))
            t.start()
            t.join()
    print("[+] Reach end of directory")

dir_upload("http://localhost/upload/","supplier-data/images")
