import requests
import json
import time
import os, sys
import threading

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)  # line buffering to avoid terminal hang

TARGET_T2_URL = "http://34.203.25.208/"
TARGET_M4_URL = "http://3.209.122.237/"
TARGET_ALL_URL = "http://3.212.147.131/"


def send_request_sync(url, count):
    index = 0
    while index < count:
        message = " | Unsuccessful Request"

        r = requests.get(url=url)
        response_code = r.status_code
        response = r.text
        if (response_code == 200):
            message = " | Successful Request"
        print(response + message)
        index += 1

    return


def run_scenario():
    url = TARGET_ALL_URL

    
    t1 = threading.Thread(target=run_scenario_one, args=("group one", TARGET_T2_URL))
    t1.start()
    t2 = threading.Thread(target=run_scenario_two, args=("group two", TARGET_M4_URL))
    t2.start()
    t1.join()
    t2.join()
    
    return


def run_scenario_one(name, url):
    print("Initiating 50 requests to " + name + " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 50)
    print("------------------------------------------------------------\n")
    return


def run_scenario_two(name, url):
    print("Initiating 150 requests to " + name + " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 150)
    print("------------------------------------------------------------\n")
    return


def main():
    print("Starting ELB test senarios...\n\n")
    print("---------------------------\n")
    print("Running Scenario 1 for group one and group two ...\n\n")
    print("---------------------------\n")
    run_scenario()
    return


main()
