import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'YOUR_S3_BUCKET_NAME'

    # Assume the file is received as base64-encoded in event['body']
    file_content = base64.b64decode(event['body'])
    file_path = 'uploaded_file.m4a'
    s3.put_object(Bucket=bucket_name, Key=file_path, Body=file_content)

    # Optional: Call OpenAI API here

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Your audio file has been received and processed'})
    }
