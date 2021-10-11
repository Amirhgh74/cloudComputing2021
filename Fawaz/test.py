import os
import json
import boto3
import tkinter
import matplotlib

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
    
    # changes size of the figure itself
    fig1, ax1 = plt.subplots(2, 2,sharex=False,sharey=False)
    fig2, ax2 = plt.subplots(2, 2,sharex=False,sharey=False)
    fig3, ax3 = plt.subplots(2, 2,sharex=False,sharey=False)
    fig4, ax4 = plt.subplots(2, 2,sharex=False,sharey=False)
    

    ax1 = ax1.flatten()
    ax2 = ax2.flatten()
    ax3 = ax3.flatten()
    ax4 = ax4.flatten()

    i = 0
    while i < 4:
        ax1[i].scatter(metric_timestamp_t2[i], metric_data_t2[i], label=(str(metric_id_t2[i]) + "_T2"))
        ax1[i].legend(frameon=True)
        plt.setp(ax1[i].get_xticklabels(), rotation=90)
        ax1[i].tick_params(axis="x", labelsize=6)
        ax1[i].xaxis.set_major_locator(MaxNLocator(nbins=10))

        ax1[i].scatter(metric_timestamp_m4[i], metric_data_m4[i], label=(str(metric_id_m4[i]) + "_M4"))
        ax1[i].legend(frameon=True)
        plt.setp(ax1[i].get_xticklabels(), rotation=90)
        ax1[i].tick_params(axis="x", labelsize=6)
        ax1[i].xaxis.set_major_locator(MaxNLocator(nbins=10))



        i += 1

    
    while 4 <= i < 8:
        j = i - 4
        ax2[j].scatter(metric_timestamp_t2[i], metric_data_t2[i], label=(str(metric_id_t2[i]) + "_T2"), s = 5)
        ax2[j].legend(frameon=True)
        plt.setp(ax2[j].get_xticklabels(), rotation=90)
        ax2[j].tick_params(axis="x", labelsize=6)
        ax2[j].xaxis.set_major_locator(MaxNLocator(nbins=10))

        ax2[j].scatter(metric_timestamp_m4[i], metric_data_m4[i], label=(str(metric_id_m4[i]) + "_M2"), s = 5)
        ax2[j].legend(frameon=True)
        plt.setp(ax2[j].get_xticklabels(), rotation=90)
        ax2[j].tick_params(axis="x", labelsize=6)
        ax2[j].xaxis.set_major_locator(MaxNLocator(nbins=10))

        i += 1

    while 8 <= i < 12:
        j = i - 8
        ax3[j].scatter(metric_timestamp_t2[i], metric_data_t2[i], label=(str(metric_id_t2[i]) + "_T2"), s = 5)
        ax3[j].legend(frameon=True)
        plt.setp(ax3[j].get_xticklabels(), rotation=90)
        ax3[j].tick_params(axis="x", labelsize=6)
        ax3[j].xaxis.set_major_locator(MaxNLocator(nbins=10))

        ax3[j].scatter(metric_timestamp_m4[i], metric_data_m4[i], label=(str(metric_id_m4[i]) + "_M2"), s = 5)
        ax3[j].legend(frameon=True)
        plt.setp(ax3[j].get_xticklabels(), rotation=90)
        ax3[j].tick_params(axis="x", labelsize=6)
        ax3[j].xaxis.set_major_locator(MaxNLocator(nbins=10))


        i += 1

    while 12 <= i < 15:
        j = i - 12
        ax4[j].scatter(metric_timestamp_t2[i], metric_data_t2[i], label=(str(metric_id_t2[i]) + "_T2"))
        ax4[j].legend(frameon=True)
        plt.setp(ax4[j].get_xticklabels(), rotation=90)
        ax4[j].tick_params(axis="x", labelsize=6)
        ax4[j].xaxis.set_major_locator(MaxNLocator(nbins=10))

        ax4[j].scatter(metric_timestamp_m4[i], metric_data_m4[i], label=(str(metric_id_m4[i]) + "_M4"))
        ax4[j].legend(frameon=True)
        plt.setp(ax4[j].get_xticklabels(), rotation=90)
        ax4[j].tick_params(axis="x", labelsize=6)
        ax4[j].xaxis.set_major_locator(MaxNLocator(nbins=10))
        


        i += 1
    
    # change spacing of the subplots
    large = 22; med = 16; small = 5
    params = {'axes.titlesize': small,
        'legend.fontsize': small,
        'figure.figsize': (20, 14),
        'axes.labelsize': small,
        'axes.titlesize': small,
        'xtick.labelsize': small,
        'ytick.labelsize': small,
        'figure.titlesize': small
        }
    plt.rcParams.update(params)

    plt.show()
    
    return 0
    

main()

