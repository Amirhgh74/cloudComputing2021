import requests
import json
import time

TARGET_T2_URL = "http://34.193.180.212:5000/"
TARGET_M4_URL = "http://34.193.180.212:8000/"
TARGET_ALL_URL = "http://34.193.180.212/"


def send_request_sync(url, count):

    index = 0
    while index < count:

        r = requests.get(url= url)
        response_code  = r.status_code
        response = r.json()
        print(response)
        print(response_code)
        index += 1

    return 


def run_senario(name):

    url = TARGET_ALL_URL

    if name == "T2":
        url = TARGET_T2_URL
    elif name == "M4":
        url ==  TARGET_M4_URL

    print("initiate 1000 request to the " + name +  " target cluster...")
    send_request_sync(url, 1000)

    print("initiate 500 request to the "  + name +  " target cluster...")
    send_request_sync(url, 500)

    print("sleep for one minute...")
    time.sleep(60)

    print ("initiate 1000 request to the " + name +  " target cluster")
    send_request_sync(url, 1000)

    return


def main():
    print("starting test senarios...\n\n")
    run_senario("T2")
    run_senario("M4")
    return 

main()