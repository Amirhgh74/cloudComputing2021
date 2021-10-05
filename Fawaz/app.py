import os
import json
import boto3
from pprint import pprint
from datetime import datetime
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt



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
RequestCountPerTarget_json = '{\
    "metrics": [\
        [ "AWS/ApplicationELB", "RequestCountPerTarget", "LoadBalancer", "app/ELB-M4-Cluster/36b97285aae53f1f",  "TargetGroup" , "targetgroup/M4-Cluster/144c46b0855b89d3" ,{ "stat": "Sum", "id": "m0" } ]\
    ],\
    "legend": {\
        "position": "bottom"\
    },\
    "period": 300,\
    "view": "timeSeries",\
    "stacked": false,\
    "title": "M4-Cluster - RequestCountPerTarget",\
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
        StartTime=datetime.utcnow() - timedelta(hours=3),
        EndTime=datetime.utcnow(),
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
    pprint(response['Datapoints']) 
    
    ## Print metric number only
<<<<<<< HEAD
    datapoint = [x['Maximum'] for x in response['Datapoints']]
    timestamp = [y['Timestamp'] for y in response['Datapoints']]
    df = pd.DataFrame({'timestamp':timestamp, 'datapoint':datapoint})
=======
    # for item in response['Datapoints']:
    # 	print (item['Maximum'])
>>>>>>> 182e40b1e5d893cfc08351ceeccdcc39d25631a3
    
    df['datapoint']  = [pd.to_numeric(i) for i in df['datapoint']]
    print(df.sort_values(by='datapoint'))
    plt.plot(datapoint)
    plt.show()
    ## Save the Graph 
    response = client.get_metric_widget_image(MetricWidget=RequestCountPerTarget_json)
    with open ('ReuqestPer.png', 'wb') as f:
    	f.write(response["MetricWidgetImage"])
    
    

    return 0



main()
