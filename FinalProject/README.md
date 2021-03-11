# FinalProject
This repository store the scripts needed for the final project on week 4 of "Automating Real-world Tasks with Python"

## Content
There are 7 scripts that is needed for the activity:
#### changeImage.py
This script is going to utilize the PIL library of Python to change the image according to the requirements:
* __Size__: From __3000x2000__ to __600x400__ pixel
* __Format__: From __.TIFF__ to __.JPEG__ <br/>

Then store the new images in the same directory as the original

### supplier_image_upload.py

Retrieve all of the __.JPEG__ images from the directory and upload them to the URL of `http://[linux-instance-IP-Address]/upload/` using the POST method

### run.py
Extract information from files inside `supplier-data/descriptions/` and use POST requests to post the data to web server at `http://[linux0instance-IP-Address]/fruits/`

### reports.py
Template for generating PDF reports

### emals.py
Template for sending emails with attachment, currently using localhost SMTP server

### report_email.py
Extract fruits name and weight from files inside `supplier-data/descriptions/` then:
* Use the _generate_report()_ method of `report.py` to create a report and store it as __"/tmp/processed.pdf"__  
* Use the _process_email()_ and _send()_ method of `emails.py` to send report to the users

### health_check.py
Utilize the psutil and shutil module of Python to constantly checking status of the system with the interval of 60 second. Then send emails to the users if:
* CPU usage is over __80%__
* Available disk space is lower than __20%__
* Available memory is less than __500MB__
* Hostname __"localhost"__ cannot be resolve to __"127.0.0.1"__
