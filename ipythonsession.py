import boto3
session = boto3.Session(profile_name='bharath-profile')
s3 = session.resource('s3')
