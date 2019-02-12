#import sys
import boto3
import click

session = boto3.Session(profile_name='PythonAutomation')
s3 = session.resource('s3')


# print(sys.argv)
@click.group()
def cli():
        "Webotron will be deploy into the AWS"
        pass

@cli.command('list-buckets')
#@click.command('list-buckets')
def list_buckets():
        "List all S3 buckets"
        for bucket in s3.buckets.all():
                print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')

def list_bucket_objects(bucket):
        "List all the S3 bucket objects"
        for obj in s3.Bucket(bucket).objects.all():
                print (obj)

if __name__ == "__main__":
        cli()
        #list_buckets()