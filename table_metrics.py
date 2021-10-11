import os
import json
import boto3
import tkinter
import matplotlib
from tabulate import tabulate
from pprint import pprint
import dateutil.tz
import dateutil.parser
from datetime import datetime
from numpy import *
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from matplotlib.ticker import MaxNLocator

def initialize_client():
    client = boto3.client(
        'cloudwatch',
        region_name='us-east-1'
    )
    return client


def get_metric_data(configurations):

    # Create CloudWatch client.
    metric_client = boto3.client("cloudwatch", region_name= 'us-east-1')

    # Make GetMetricData API request.
    metric_data = metric_client.get_metric_data(
        StartTime = (datetime.utcnow() - timedelta(minutes=10)),
        EndTime = (datetime.utcnow()),
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
    
    print("Reading AWS Metrics and Drawing Data")


    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file1 = json.load(open("ec2_m4.json", "r"))

    # pprint(json_file)
    response1 = get_metric_data(json_file1)
    size1 = len (response1['MetricDataResults'])

    # pprint(response1)

    for i in range(0, size1):
        metric_id_m4.append(response1['MetricDataResults'][i]['Id'])
        metric_data_m4.append(response1['MetricDataResults'][i]['Values'])
        

          
    # Read 1 Metric and print it
    json_file2 = json.load(open("ec2_t2.json", "r"))

    # pprint(json_file)

    response2 = get_metric_data(json_file2)
    size2 = len (response2['MetricDataResults'])

    for i in range(0, size1):
        metric_id_t2.append(response2['MetricDataResults'][i]['Id'])
        metric_data_t2.append(response2['MetricDataResults'][i]['Values'])
        

    table1 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table2 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table3 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table4 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    table5 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table6 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table7 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    table8 = [["METRIC", "COUNT"],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    
    i = 0
    while i < 13:
        table1[i+1].append(metric_id_m4[i])
        sum = 0
        for x in metric_data_m4[i]:
            sum += x
        table1[i+1].append(sum)
        i += 1

    while 13 <= i < 26:
        table2[(i-13)+1].append(metric_id_m4[i])
        sum = 0
        for x in metric_data_m4[i]:
            sum += x
        table2[(i-13)+1].append(sum)
        i += 1

    while 26<= i < 39:
        table3[(i-26)+1].append(metric_id_m4[i])
        sum = 0
        for x in metric_data_m4[i]:
            sum += x
        table3[(i-26)+1].append(sum)
        i += 1

    while 39 <= i < 52:
        table4[(i-39)+1].append(metric_id_m4[i])
        sum = 0
        for x in metric_data_m4[i]:
            sum += x
        table4[(i-39)+1].append(sum)
        i += 1


    print("M4 CLUSTER INSTANCE METRICS" ,file=open("output.txt", "a"))

    print("\n" , file=open("output.txt", "a"))
    print(tabulate(table1,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))
    print(tabulate(table2,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))
    
    print(tabulate(table3,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))

    print(tabulate(table4,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))


    i = 0
    while i < 13:
        table5[i+1].append(metric_id_t2[i])
        sum = 0
        for x in metric_data_t2[i]:
            sum += x
        table5[i+1].append(sum)
        i += 1

    while 13 <= i < 26:
        table6[(i-13)+1].append(metric_id_t2[i])
        sum = 0
        for x in metric_data_t2[i]:
            sum += x
        table6[(i-13)+1].append(sum)
        i += 1

    while 26<= i < 39:
        table7[(i-26)+1].append(metric_id_t2[i])
        sum = 0
        for x in metric_data_t2[i]:
            sum += x
        table7[(i-26)+1].append(sum)
        i += 1

    while 39 <= i < 52:
        table8[(i-39)+1].append(metric_id_t2[i])
        sum = 0
        for x in metric_data_t2[i]:
            sum += x
        table8[(i-39)+1].append(sum)
        i += 1

    print("T2 CLUSTER INSTANCE METRICS" ,file=open("output.txt", "a"))

    print("\n" , file=open("output.txt", "a"))
    print(tabulate(table5,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))
    print(tabulate(table6,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))
    
    print(tabulate(table7,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))

    print(tabulate(table8,headers='firstrow', tablefmt='grid'), file=open("output.txt", "a"))
    print("\n" , file=open("output.txt", "a"))




    return 0
    

main()

