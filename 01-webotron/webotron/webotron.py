#! /usr/bin/python

# -*- coding: utf-8 -*-

"""Webotron: Deploy websites with aws.

Webotron automates the process of deploying a static website in AWS

- Configure AWS S3 buckets
        - create them
        - set up them for static web hosting
        - deploy local files to them
- configure DNS with AWS route 53
- configure content delivery network and SSL with AWS Cloudfront

"""
from pathlib import Path
import mimetypes

import boto3
from botocore.exceptions import ClientError
import click


session = boto3.Session(profile_name='bharath')
s3 = session.resource('s3')


@click.group()
def cli():
        """Webotron will be deployed in AWS."""
        pass


@cli.command("list-buckets")
def list_buckets():
        """List of buckets."""
        for bucket in s3.buckets.all():
                print(bucket)


@click.argument("bucket")

@cli.command("list-bucket-objects")
def list_bucket_objects(bucket):
        """List all the bucket objects."""
        for obj in s3.Bucket(bucket).objects.all():
                print(obj)


@cli.command("setup-bucket")
@click.argument("bucket")
def setup_bucket(bucket):
        """Create and configure S3 bucket."""
        s3_bucket = None

        try:
                s3_bucket = s3.create_bucket(
                        Bucket=bucket, 
                        CreateBucketConfiguration={
                                'LocationConstraint': session.region_name
                        }
                )

        except ClientError as e:
                if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                        s3_bucket = s3.Bucket(bucket)
                else:
                        raise e

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
        """ % s3_bucket.name

        policy = policy.strip()

        pol = s3_bucket.Policy()
        pol.put(Policy=policy)

        ws = s3_bucket.Website()
        ws.put(WebsiteConfiguration={
                'ErrorDocument': {
                        'Key': 'error.html'
                },
                'IndexDocument': {
                        'Suffix': 'index.html'
                }
        })

        return


def upload_file(s3_bucket, path, key):
        content_type = mimetypes.guess_type(key)[0] or "text/plain"
        s3_bucket.upload_file(
                path,
                key,
                ExtraArgs={
                        "ContentType": content_type
                })


@cli.command("sync")
@click.argument("pathname", type=click.Path(exists=True))
@click.argument("bucket")
def sync(pathname, bucket):
        """Sync contents of PATHNAME to BUCKET."""

        s3_bucket = s3.Bucket(bucket)

        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):
                for p in target.iterdir():
                        if p.is_dir(): 
                                handle_directory(p)
                        if p.is_file(): 
                                upload_file(s3_bucket, str(p), str(p.relative_to(root)))

        handle_directory(root)


if __name__ == "__main__":
        cli()



        