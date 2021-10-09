import boto3
from datetime import datetime
from datetime import timedelta



client = boto3.client(service_name='cloudwatch', region_name='us-east-1')

# response = client.get_metric_statistics(
#     Namespace = 'AWS/ApplicationELB',
#     Period = 3600,
#     StartTime = datetime.utcnow() - timedelta(seconds = 600),
#     EndTime = datetime.utcnow(),
#     MetricName = "UnHealthyHostCount",
#     Statistics=['Average'],
#     Dimensions = [
#         {'Name': 'myELB', 'Value': "loadbalancer/app/myELB/9fc56dae0bbb2740"}
#     ])


paginator = client.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   MetricName='IncomingLogEvents',
                                   Namespace='AWS/Logs'):
    print(response['Metrics'])


print(response)