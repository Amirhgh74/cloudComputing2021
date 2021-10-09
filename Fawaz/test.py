import os
import json
import boto3
from pprint import pprint
import dateutil.tz
import dateutil.parser
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


def initialize_client():
    client = boto3.client(
        'cloudwatch',
        region_name='us-east-1'
    )
    return client




def get_metric_data(configurations):

    # Create CloudWatch client.
    metric_client = boto3.client("cloudwatch")

    # Make GetMetricData API request.
    metric_data = metric_client.get_metric_data(
        **configurations
    )
    return metric_data



def main():
    metric_id = []
    metric_data = []
    temp = []
    metric_timestamp = []

    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file = json.load(open("fil.json", "r"))

    # pprint(json_file)

    response = get_metric_data(json_file)
    size = len (response['MetricDataResults'])

    for i in range(0, size):
        metric_id.append(response['MetricDataResults'][i]['Id'])
        metric_data.append(response['MetricDataResults'][i]['Values'])
        temp = [z.strftime("%H:%M:%S") for z in (response['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp.append(temp)   

        

    print("First Parameter\n")
    print ("ID = ", metric_id[0])
    print ("Value = ", metric_data[0])
    print ("Timestamp = ", metric_timestamp[0])
    print("\n\n")
    print("Second Parameter\n")
    print ("ID = ", metric_id[1])
    print ("Value = ", metric_data[1])
    print ("Timestamp = ", metric_timestamp[1])
    return 0



main()

