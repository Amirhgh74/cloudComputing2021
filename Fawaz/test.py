import os
import json
import boto3
from pprint import pprint
import dateutil.tz
import dateutil.parser
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone

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
        StartTime = (datetime.utcnow() - timedelta(hours=3)),
        EndTime = datetime.utcnow(),
        **configurations
    )
    return metric_data



def main():
    metric_id_m4 = []
    metric_data_m4 = []
    metric_timestamp_m4 = []
    temp1=[]
    temp2=[]
    metric_id_t2 = []
    metric_data_t2 = []
    metric_timestamp_t2 = []


    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file1 = json.load(open("m4_cluster.json", "r"))

    # pprint(json_file)
    response1 = get_metric_data(json_file1)
    size1 = len (response1['MetricDataResults'])

    for i in range(0, size1):
        metric_id_m4.append(response1['MetricDataResults'][i]['Id'])
        metric_data_m4.append(response1['MetricDataResults'][i]['Values'])
        temp1 = [z.strftime("%H:%M:%S") for z in (response1['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_m4.append(temp1) 

          
    # Read 1 Metric and print it
    json_file2 = json.load(open("t2_cluster.json", "r"))

    # pprint(json_file)

    response2 = get_metric_data(json_file2)
    size2 = len (response2['MetricDataResults'])

    for i in range(0, size1):
        metric_id_t2.append(response2['MetricDataResults'][i]['Id'])
        metric_data_t2.append(response2['MetricDataResults'][i]['Values'])
        temp2 = [z.strftime("%H:%M:%S") for z in (response2['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_t2.append(temp2)
    

    fig, axs = plt.subplots(5, 3)
    axs = axs.flatten()
    for i in range(15):
        axs[i].plot(metric_timestamp_t2[i], metric_data_t2[i], label=metric_id_t2[i])
        axs[i].plot(metric_timestamp_m4[i], metric_data_m4[i], label=metric_id_m4[i])
    plt.show()
    
    
    return 0



main()

