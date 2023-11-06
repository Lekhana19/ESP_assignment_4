import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'serverlesstestbkt-1'
    keys = ['cat1.jpeg', 'cat2.jpeg', 'cat3.jpeg'] 

    image_sizes = {} 

    for key in keys:
        response = s3.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        image_size = len(image_data)

        image_sizes[key] = image_size 

    return {
        'statusCode': 200,
        'body': json.dumps(image_sizes)
    }

