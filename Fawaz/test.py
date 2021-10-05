import os
import json
import boto3
from pprint import pprint
from datetime import datetime, timedelta


def get_metric_data(configurations):

    # Create CloudWatch client.
    metric_client = boto3.client("cloudwatch")

    # Make GetMetricData API request.
    metric_data = metric_client.get_metric_data(
        **configurations
    )
    return metric_data
    
    

json_file = json.load(open("fil.json", "r"))


cloudwatch  = boto3.client('cloudwatch', region_name='us-east-1')


response = get_metric_data(json_file)

pprint(response)
