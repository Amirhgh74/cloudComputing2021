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
        region_name='us-east-1c'
    )
    return client


def get_metric_data(configurations):

    # Create CloudWatch client.
    metric_client = boto3.client("cloudwatch", region_name= 'us-east-1')

    # Make GetMetricData API request.
    metric_data = metric_client.get_metric_data(
        StartTime = (datetime.utcnow() - timedelta(hours = 8)),
        EndTime = (datetime.utcnow()),
        **configurations
    )
    return metric_data



def main():
    metric_id_m4_elb = []
    metric_data_m4_elb = []
    metric_timestamp_m4_elb = []
    temp1=[]
    temp2=[]
    metric_id_t2_elb = []
    metric_data_t2_elb = []
    metric_timestamp_t2_elb = []



    metric_id_m4_ec2 = []
    metric_data_m4_ec2 = []
    metric_timestamp_m4_ec2 = []
    temp3=[]
    temp4=[]
    metric_id_t2_ec2 = []
    metric_data_t2_ec2 = []
    metric_timestamp_t2_ec2 = []
    
    print("Reading AWS Metrics and Drawing Data")


    client = initialize_client()
    
    # Read 1 Metric and print it
    json_file1 = json.load(open("ec2_cluster_1.json", "r"))

    # pprint(json_file)
    response1 = get_metric_data(json_file1)
    size1 = len (response1['MetricDataResults'])

    for i in range(0, size1):
        metric_id_m4_elb.append(response1['MetricDataResults'][i]['Id'])
        metric_data_m4_elb.append(response1['MetricDataResults'][i]['Values'])
        temp1 = [z.strftime("%H:%M:%S") for z in (response1['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_m4_elb.append(temp1) 

          
    # Read 1 Metric and print it
    json_file2 = json.load(open("ec2_cluster_2.json", "r"))

    # pprint(json_file)

    response2 = get_metric_data(json_file2)
    size2 = len (response2['MetricDataResults'])

    for i in range(0, size1):
        metric_id_t2_elb.append(response2['MetricDataResults'][i]['Id'])
        metric_data_t2_elb.append(response2['MetricDataResults'][i]['Values'])
        temp2 = [z.strftime("%H:%M:%S") for z in (response2['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_t2_elb.append(temp2)

    # changes size of the figure itself
    fig1, ax1 = plt.subplots(2, 2,sharex=False,sharey=False, num="ELB Metrics 1")
    fig2, ax2 = plt.subplots(2, 2,sharex=False,sharey=False, num="ELB Metrics 2")
    fig3, ax3 = plt.subplots(2, 2,sharex=False,sharey=False, num="ELB Metrics 3")
    fig4, ax4 = plt.subplots(2, 2,sharex=False,sharey=False, num="ELB Metrics 4")
    

    ax1 = ax1.flatten()
    ax2 = ax2.flatten()
    ax3 = ax3.flatten()
    ax4 = ax4.flatten()

    i = 0
    while i < 4:
        ax1[i].scatter(metric_timestamp_t2_elb[i], metric_data_t2_elb[i], label=(str(metric_id_t2_elb[i]) + "_Grp2"), s = 8)
        ax1[i].legend(frameon=True)
        ax1[i].scatter(metric_timestamp_m4_elb[i], metric_data_m4_elb[i], label=(str(metric_id_m4_elb[i]) + "_Grp1"), s = 8)
        ax1[i].legend(frameon=True)
        plt.setp(ax1[i].get_xticklabels(), rotation=90)
        ax1[i].tick_params(axis="x", labelsize=6)
        ax1[i].xaxis.set_major_locator(MaxNLocator(nbins=10))



        i += 1

    
    while 4 <= i < 8:
        j = i - 4
        ax2[j].scatter(metric_timestamp_t2_elb[i], metric_data_t2_elb[i], label=(str(metric_id_t2_elb[i]) + "_Grp2"), s = 8)
        ax2[j].scatter(metric_timestamp_m4_elb[i], metric_data_m4_elb[i], label=(str(metric_id_m4_elb[i]) + "_Grp1"), s = 8)
        ax2[j].legend(frameon=True)
        plt.setp(ax2[j].get_xticklabels(), rotation=90)
        ax2[j].tick_params(axis="x", labelsize=6)
        ax2[j].xaxis.set_major_locator(MaxNLocator(nbins=10))

        i += 1

    while 8 <= i < 12:
        j = i - 8
        ax3[j].scatter(metric_timestamp_t2_elb[i], metric_data_t2_elb[i], label=(str(metric_id_t2_elb[i]) + "_Grp2"), s = 8)
        ax3[j].scatter(metric_timestamp_m4_elb[i], metric_data_m4_elb[i], label=(str(metric_id_m4_elb[i]) + "_Grp1"), s = 8)
        ax3[j].legend(frameon=True)
        plt.setp(ax3[j].get_xticklabels(), rotation=90)
        ax3[j].tick_params(axis="x", labelsize=6)
        ax3[j].xaxis.set_major_locator(MaxNLocator(nbins=10))


        i += 1

    while 12 <= i < 15:
        j = i - 12
        ax4[j].scatter(metric_timestamp_t2_elb[i], metric_data_t2_elb[i], label=(str(metric_id_t2_elb[i]) + "_Grp2"), s = 8)
        ax4[j].scatter(metric_timestamp_m4_elb[i], metric_data_m4_elb[i], label=(str(metric_id_m4_elb[i]) + "_Grp1"), s = 8)
        ax4[j].legend(frameon=True)
        plt.setp(ax4[j].get_xticklabels(), rotation=90)
        ax4[j].tick_params(axis="x", labelsize=6)
        ax4[j].xaxis.set_major_locator(MaxNLocator(nbins=10))
        i += 1

    #### Get Instance Metrics#####

    # Read 1 Metric and print it
    json_file3 = json.load(open("ec2_1.json", "r"))
    response3 = get_metric_data(json_file3)
    size3 = len (response3['MetricDataResults'])

    for i in range(size3):
        metric_id_m4_ec2.append(response3['MetricDataResults'][i]['Id'])
        metric_data_m4_ec2.append(response3['MetricDataResults'][i]['Values'])
        temp3 = [z.strftime("%H:%M:%S") for z in (response3['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_m4_ec2.append(temp3)
    
    # Read 1 Metric and print it
    json_file4 = json.load(open("ec2_2.json", "r"))
    response4 = get_metric_data(json_file4)
    size4 = len (response4['MetricDataResults'])

    for i in range(size4):
        metric_id_t2_ec2.append(response4['MetricDataResults'][i]['Id'])
        metric_data_t2_ec2.append(response4['MetricDataResults'][i]['Values'])
        temp4 = [z.strftime("%H:%M:%S") for z in (response4['MetricDataResults'][i]['Timestamps'])]  
        metric_timestamp_t2_ec2.append(temp4)

    ##HERE
    # changes size of the figure itself
    fig5, ax5 = plt.subplots(2, 2,sharex=False,sharey=False, num="EC2 Metrics 1")
    fig6, ax6 = plt.subplots(2, 2,sharex=False,sharey=False, num="EC2 Metrics 2")
    fig7, ax7 = plt.subplots(2, 2,sharex=False,sharey=False, num="EC2 Metrics 3")
    fig8, ax8 = plt.subplots(2, 2,sharex=False,sharey=False, num="EC2 Metrics 3")

    ax5 = ax5.flatten()
    ax6 = ax6.flatten()
    ax7 = ax7.flatten()
    ax8 = ax8.flatten()

    a = 0
    
    while a < 4:
        for  b in range (a, len(metric_id_t2_ec2), 13):
            ax5[a].scatter(metric_timestamp_t2_ec2[b], metric_data_t2_ec2[b], label =str(metric_id_t2_ec2[b]), s = 8)
            ax5[a].scatter(metric_timestamp_m4_ec2[b], metric_data_m4_ec2[b], label=str(metric_id_m4_ec2[b]), s = 8)
        ax5[a].legend(frameon=True)
        ax5[a].tick_params(axis="x", labelsize=6)
        ax5[a].legend(frameon=True)
        plt.setp(ax5[a].get_xticklabels(), rotation=90)
        ax5[a].tick_params(axis="x", labelsize=6)
        ax5[a].xaxis.set_major_locator(MaxNLocator(nbins=10))

        a += 1
    a = 0
    while a < 4:
        for  b in range (a+4, len(metric_id_t2_ec2), 13):
            ax6[a].scatter(metric_timestamp_t2_ec2[b], metric_data_t2_ec2[b], label =str(metric_id_t2_ec2[b]), s = 8)
            ax6[a].scatter(metric_timestamp_m4_ec2[b], metric_data_m4_ec2[b], label=str(metric_id_m4_ec2[b]), s = 8)
        ax6[a].legend(frameon=True)
        ax6[a].tick_params(axis="x", labelsize=6)
        ax6[a].legend(frameon=True)
        plt.setp(ax6[a].get_xticklabels(), rotation=90)
        ax6[a].tick_params(axis="x", labelsize=6)
        ax6[a].xaxis.set_major_locator(MaxNLocator(nbins=10))

        a += 1
    a = 0
    while a < 4:
        for  b in range (a+8, len(metric_id_t2_ec2), 13):
            ax7[a].scatter(metric_timestamp_t2_ec2[b], metric_data_t2_ec2[b], label =str(metric_id_t2_ec2[b]), s = 8)
            ax7[a].scatter(metric_timestamp_m4_ec2[b], metric_data_m4_ec2[b], label=str(metric_id_m4_ec2[b]), s = 8)
        ax7[a].legend(frameon=True)
        ax7[a].tick_params(axis="x", labelsize=6)
        ax7[a].legend(frameon=True)
        plt.setp(ax7[a].get_xticklabels(), rotation=90)
        ax7[a].tick_params(axis="x", labelsize=6)
        ax7[a].xaxis.set_major_locator(MaxNLocator(nbins=10))
        a += 1
    a = 0
    while a < 4:
        for  b in range (a+12, len(metric_id_t2_ec2), 13):
            ax8[a].scatter(metric_timestamp_t2_ec2[b], metric_data_t2_ec2[b], label =str(metric_id_t2_ec2[b]), s = 8)
            ax8[a].scatter(metric_timestamp_m4_ec2[b], metric_data_m4_ec2[b], label=str(metric_id_m4_ec2[b]), s = 8)
        ax8[a].legend(frameon=True)
        ax8[a].tick_params(axis="x", labelsize=6)
        ax8[a].legend(frameon=True)
        plt.setp(ax8[a].get_xticklabels(), rotation=90)
        ax8[a].tick_params(axis="x", labelsize=6)
        ax8[a].xaxis.set_major_locator(MaxNLocator(nbins=10))
        a += 1

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


