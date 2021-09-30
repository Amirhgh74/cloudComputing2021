import boto3 

# client = boto3.client('ec2-instance-connect')

# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-east-1',
#     aws_access_key_id='ID',
#     aws_secret_access_key='KEY'
# )

# for bucket in s3.buckets.all():
#     print(bucket.name)


ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response["Reservations"][0]["Instances"][0]["InstanceId"])