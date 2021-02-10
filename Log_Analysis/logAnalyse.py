#!/usr/bin/env python3
import re
import operator
import csv

def find_error(log):
    """Extract error log for the ticking service and sort them according to theirs count"""
    with open(log,"r") as log_file:
        error_dict={}
        #Declare regex to extract information
        keyword=r"ticky: ERROR (.*)?\(.*\)"

        #Iterate through the log file 
        for message in log_file.readlines():
            errors=re.search(keyword,message)
            
            #If the match is caught -> Add the error and increase the counter
            if errors:
                error_dict[errors.group(1)]=error_dict.get(errors.group(1),0)+1
    
    #Return the errors sorted by the most occured issue
    return sorted(error_dict.items(),key=operator.itemgetter(1),reverse=True)

def user_activity(log):
    """Extract users statistics for the ticking service"""
    
    #Iterate throught the log file
    with open(log,"r") as log_file:
        user_dict={}
        #Declare the regex to extract information
        keyword=r"ticky: (INFO|ERROR) (.*)?\((.*)\)$"
        for message in log_file.readlines():
            act=re.search(keyword,message)

            #Extract the user statistic and add them to the dictionary
            if act:
                #Get user and message type
                user=act.group(3)
                mtype=act.group(1)

                #If the user is not added to the dictionary -> Add them
                if user not in user_dict:
                    user_dict[user]={}
                user_dict[user][mtype]=user_dict[user].get(mtype,1)+1
    
    #Return the sorted user statistics
    return sorted(user_dict.items())

def generate_report(log,error_out,user_out):
    """Generate the report base on the errors and user statisics"""
    error_dict=find_error(log)
    with open(error_out,"w+") as error_file:
        error_writer=csv.writer(error_file)
        #Write the csv file header
        error_writer.writerow(["Error","Count"])
        for error, count in error_dict:
            error_writer.writerow([error,count])

    user_dict=user_activity(log)
    with open(user_out,"w+") as user_file:
        user_writer=csv.writer(user_file)
        #Write the csv file header
        user_writer.writerow(["Username","INFO","ERROR"])
        for user,activity in user_dict:
            user_writer.writerow([user,activity.get("INFO",0),activity.get("ERROR",0)])


error_file=input("Enter your error message filename: ")
user_file=input("Enter your user statistic filename: "
generate_report("syslog.log",error_file,user_file)
                   
