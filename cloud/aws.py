import boto3

def create_bucket(bucket_name):
    """Create a new S3 bucket"""
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created.")

def upload_file(bucket_name, local_file_path, destination_file_name):
    """Upload a local file to the specified S3 bucket"""
    s3_client = boto3.client('s3')
    s3_client.upload_file(local_file_path, bucket_name, destination_file_name)
    print(f"File '{local_file_path}' uploaded to '{bucket_name}/{destination_file_name}'.")

def download_file(bucket_name, file_name, destination_file_path):
    """Download a file from the specified S3 bucket"""
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name, file_name, destination_file_path)
    print(f"File '{bucket_name}/{file_name}' downloaded to '{destination_file_path}'.")

def list_files(bucket_name):
    """List all files in the specified S3 bucket"""
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    print(f"Files in bucket '{bucket_name}':")
    for file in response['Contents']:
        print(file['Key'])

def delete_file(bucket_name, file_name):
    """Delete a file from the specified S3 bucket"""
    s3_client = boto3.client('s3')
    s3_client.delete_object(Bucket=bucket_name, Key=file_name)
    print(f"File '{bucket_name}/{file_name}' deleted.")

if __name__ == '__main__':
    # Set your bucket name
    bucket_name = 'your-bucket-name'

    # Create a new bucket
    create_bucket(bucket_name)

    # Upload a file
    local_file_path = 'path/to/local/file.txt'
    destination_file_name = 'file.txt'
    upload_file(bucket_name, local_file_path, destination_file_name)

    # Download a file
    file_name = 'file.txt'
    destination_file_path = 'path/to/destination/file.txt'
    download_file(bucket_name, file_name, destination_file_path)

    # List all files in the bucket
    list_files(bucket_name)

    # Delete a file from the bucket
    delete_file(bucket_name, file_name)
