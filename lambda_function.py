import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Extract bucket name and file key from event
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
    except KeyError:
        return {
            'statusCode': 400,
            'body': 'Invalid event structure. Make sure the test event is correct.'
        }

    # Read CSV File from S3
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_csv(response['Body'])
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error reading CSV file: {str(e)}'
        }

    # Data Cleaning - Remove Null Values
    df.dropna(inplace=True)

    # Save Processed Data to S3
    output_key = file_key.replace("raw_data/", "processed-data/")  # Save to processed-data folder
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    try:
        s3.put_object(Bucket=bucket_name, Key=output_key, Body=csv_buffer.getvalue())
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error saving processed data: {str(e)}'
        }

    return {
        'statusCode': 200,
        'body': f'Data processed successfully and saved to {output_key}'
    }
