import boto3

def upload_to_s3(bucket, file_name, key_name):
    s3 = boto3.client("s3")
    s3.upload_file(file_name, bucket, key_name)
    print(f"Uploaded {file_name} to s3://{bucket}/{key_name}")

# upload_to_s3("my-bucket", "backup.tar.gz", "backups/backup.tar.gz")
