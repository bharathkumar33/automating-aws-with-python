# coding: utf-8
import boto3
session = boto3.Session(profile_name='Bharath-profile')
session = boto3.Session(profile_name='bharath-profile')
s3 = session.resource('S3')
s3 = session.resource('s3')
for bucket in s3.bucket.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingaws-bharath-boto3')
