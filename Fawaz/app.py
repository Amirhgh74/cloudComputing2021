import os
import json
import boto3
from pprint import pprint
from datetime import datetime
from datetime import timedelta


ConsumedLCUs_json = '{\
    "metrics": [\
        [ "AWS/ApplicationELB", "ConsumedLCUs", "LoadBalancer", "app/ELB-M4-Cluster/36b97285aae53f1f", { "stat": "Average", "id": "m0" } ]\
    ],\
    "legend": {\
        "position": "bottom"\
    },\
    "period": 300,\
    "view": "timeSeries",\
    "stacked": false,\
    "title": "All resources - ConsumedLCUs",\
    "region": "us-east-1"\
}'

def initialize_client():
    client = boto3.client(
        'cloudwatch',
        region_name='us-east-1'
    )

    return client

##### Request ConsumedLCUs metric
def request_metric(client):
    response = client.get_metric_statistics(
        Namespace='AWS/ApplicationELB',
        Period=300,
        StartTime=datetime.utcnow() - timedelta(days=5),
        EndTime=datetime.utcnow() - timedelta(days=1),
        MetricName='ConsumedLCUs',
        Statistics=['Maximum'],
        Dimensions=[
            {
                'Name': 'LoadBalancer',
                'Value': 'app/ELB-M4-Cluster/36b97285aae53f1f'
            }
            ],
    )

    return response




def main():
    client = initialize_client()
    response = request_metric(client)
    ## Print output as log file
    #pprint(response['Datapoints']) 
    
    ## Print metric number only
    for item in response['Datapoints']:
    	print (item['Maximum'])
    
    ## Save the Graph 
    response = client.get_metric_widget_image(MetricWidget=ConsumedLCUs_json)
    with open ('ConsumedLUs.png', 'wb') as f:
    	f.write(response["MetricWidgetImage"])
    
    

    return 0



main()
