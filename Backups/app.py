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
    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file = json.load(open("fil.json", "r"))

    # pprint(json_file)

    response = get_metric_data(json_file)
    pprint(response)
    print("Values =")

    size = len (response['MetricDataResults'])

    for i in range(size):

        result = response['MetricDataResults'][i]

        datapoint = result['Values'] 
        timestamp = result['Timestamps']
        timestamp = [z.strftime("%H:%M:%S") for z in timestamp]
        plt.plot(timestamp, datapoint)
        plt.xticks(rotation=90)


    # df = pd.DataFrame({'timestamp':timestamp, 'datapoint':datapoint})
    # for item in response['Datapoints']:
    # 	print (item['Maximum'])
    
    # df['datapoint']  = [pd.to_numeric(i) for i in df['datapoint']]
    #print(df.sort_values(by='datapoint'))
    # plt.plot(datapoint)
    plt.savefig('result_multiple.png')
    plt.show()
    

    return 0



main()
