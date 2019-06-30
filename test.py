# coding: utf-8
import boto3
session = boto3.Session(profile_name='PythonAutomation')
s3 = session.resource('s3')
session.region_name
new_bucket = s3.create_bucket(Bucket='automatingawsbharath-newbucket', CreateBucketConfiguration={'LocationConstraint': session.region_name})
new_bucket.upload_file('index.html','index.html',ExtraArgs={'ContentType': 'text/html'})
policy = """
{
    "Version":"2012-10-17",
    "Statement":[{
    "Sid":"PublicReadGetObject",
    "Effect":"Allow",
    "Principal": "*",
        "Action":["s3:GetObject"],
        "Resource":["arn:aws:s3:::%s/*"
        ]
        }
    ]
    }
""" % new_bucket.name
print(policy)
policy
policy = policy.strip()
pol = new_bucket.Policy()
pol.put(Policy=policy)
ws =new_bucket.Website()
ws.put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }})
url = "http://%s.s3-website.us-east-2.amazonaws.com" % new_bucket.name
url

bucket = 'automatingawsbharath-newbucket'
s3_bucket = s3.create_bucket(
                Bucket=bucket, 
                CreateBucketConfiguration={'LocationConstraint': session.region_name}
                )
from botocore.exceptions import ClientError
try:
    s3_bucket = s3.create_bucket(
                Bucket=bucket, 
                CreateBucketConfiguration={'LocationConstraint': session.region_name}
                )
except ClientError as e:
    print(e)
try:
    s3_bucket = s3.create_bucket(
                Bucket=bucket, 
                CreateBucketConfiguration={'LocationConstraint': session.region_name}
                )
except ClientError as e:
    print(e.response)
try:
    s3_bucket = s3.create_bucket(
                Bucket=bucket, 
                CreateBucketConfiguration={'LocationConstraint': session.region_name}
                )
except ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
        s3_bucket = s3.Bucket(bucket)
    else:
        raise e
