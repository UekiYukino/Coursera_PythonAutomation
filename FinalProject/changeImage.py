#!/usr/bin/env python3

from PIL import Image
import PIL
import os
def edit_image(image,new_image):
    """Configure the input image according to the activity requirement"""
    try:
        data_image=Image.open(image)
        data_image.resize((600,400)).convert("RGB").save(new_image)
        print("[+] Successfully convert {} to {}".format(image,new_image))
    except PIL.UnidentifiedImageError:
        print("[+] {} is not an image! Skipping".format(image))

def process_image(in_dir):
    """Go through the input directory and edit each image according to the requirements"""
    for image in os.listdir(in_dir):
        #Join the input directory with the image name to get the image path to process
        image_name=os.path.join(in_dir,image)
        #Skip directories
        if not os.path.isdir(image_name):
            new_name=image.replace("tiff","jpeg")
            new_image=os.path.join(in_dir,new_name)
            edit_image(image_name,new_image)

process_image("supplier-data/images")
