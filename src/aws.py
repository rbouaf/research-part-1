import boto3
import os
# import data.aws.credentials as credentials

# this is spaghetti code from chatgpt to interact with AWS

def upload_to_s3(file_path, bucket_name, s3_key):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Failed to upload {file_path} to s3://{bucket_name}/{s3_key}")
        print(e)

# Folder containing the images to upload
folder_path = "downloaded_images"

# S3 bucket name
bucket_name = "your-s3-bucket-name"

# Upload each file in the folder to S3
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        s3_key = f"images/{file_name}"  # S3 key (path in the bucket)
        upload_to_s3(file_path, bucket_name, s3_key)
