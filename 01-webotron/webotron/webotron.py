import boto3
import click

session = boto3.Session(profile_name='bharath')
s3 = session.resource('s3')

@click.group()
def cli():
        "Webotron will be deployed in AWS"
        pass

@cli.command("list-buckets")
def list_buckets():
        "list of buckets"
        for bucket in s3.buckets.all():
                print(bucket)

@click.argument("bucket")

@cli.command("list-bucket-objects")
def list_bucket_objects(bucket):
        "list all the bucket objects"
        for obj in s3.Bucket(bucket).objects.all():
                print (obj)

if __name__ == "__main__":
        cli()



