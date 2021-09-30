import requests
import json
import time
import os,sys


sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1) # line buffering to avoid terminal hang

TARGET_T2_URL = "http://52.4.16.234/"
TARGET_M4_URL = "http://3.215.104.93/"
TARGET_ALL_URL = "http://3.212.147.131/"


def send_request_sync(url, count):

    index = 0
    while index < count:
        message = " | Unsuccessful Request"

        r = requests.get(url= url)
        response_code  = r.status_code
        response = r.text
        if (response_code == 200):
        	message = " | Successful Request"
        print(response + message)
        index += 1

    return 


def run_senario(name):

    url = TARGET_ALL_URL

    if name == "T2":
        url = TARGET_T2_URL
    elif name == "M4":
        url = TARGET_M4_URL

    print("Initiating 1000 requests to " + name +  " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 1000)
    print("------------------------------------------------------------\n")
    print("Initiating 500 requests to "  + name +  " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 500)
    print("------------------------------------------------------------\n")
    print("\n---Sleeping for one minute ...\n")
    time.sleep(60)

    print ("Initiating 500 requests to " + name +  " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 1000)
    print("------------------------------------------------------------\n\n")
    return


def main():
    print("Starting ELB test senarios...\n\n")
    print("T2 Cluster Test")
    print("---------------------------\n")
    run_senario("T2")
    print("M4 Cluster Test")
    print("---------------------------\n")
    run_senario("M4")
    return 

main()
