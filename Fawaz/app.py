import os
import json
import boto3
from pprint import pprint

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
    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file = json.load(open("fil.json", "r"))
    response = get_metric_data(json_file)
    pprint(response)
    print("Values =")
    for item in response['MetricDataResults']:
        print (item['Values'])
    
    print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    
    ## Print metric number only
    datapoint = [x['Values'] for x in response['MetricDataResults']]
    timestamp = [y['Timestamps'] for y in response['MetricDataResults']]
    print("Timestamp = ")
    print(timestamp)
    df = pd.DataFrame({'timestamp':timestamp, 'datapoint':datapoint})
    # for item in response['Datapoints']:
    # 	print (item['Maximum'])
    
    df['datapoint']  = [pd.to_numeric(i) for i in df['datapoint']]
    #print(df.sort_values(by='datapoint'))
    plt.plot(datapoint)
    plt.show()

    return 0



main()
