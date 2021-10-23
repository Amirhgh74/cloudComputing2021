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


def run_scenario(name):
    url = TARGET_ALL_URL

    if name == "one":
        t1 = threading.Thread(target=run_scenario_one, args=("T2", TARGET_T2_URL))
        t1.start()
        t2 = threading.Thread(target=run_scenario_one, args=("M4", TARGET_M4_URL))
        t2.start()
        t1.join()
        t2.join()
    elif name == "two":
        t1 = threading.Thread(target=run_scenario_two, args=("T2", TARGET_T2_URL))
        t1.start()
        t2 = threading.Thread(target=run_scenario_two, args=("M4", TARGET_M4_URL))
        t2.start()
        t1.join()
        t2.join()
    return


def run_scenario_one(name, url):
    print("Initiating 1000 requests to " + name + " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 1000)
    print("------------------------------------------------------------\n")
    return


def run_scenario_two(name, url):
    print("Initiating 500 requests to " + name + " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 500)
    print("------------------------------------------------------------\n")
    print("\n---Sleeping for one minute ...\n")
    time.sleep(60)

    print("Initiating 1000 requests to " + name + " cluster ...")
    print("------------------------------------------------------------\n")
    send_request_sync(url, 1000)
    print("------------------------------------------------------------\n\n")
    return


def main():
    print("Starting ELB test senarios...\n\n")
    print("---------------------------\n")
    print("Running Scenario 1 for T2 and M4...\n\n")
    print("---------------------------\n")
    run_scenario("one")
    print("Running Scenario 2 for T2 and M4...\n\n")
    print("---------------------------\n")
    run_scenario("two")
    return


main()
