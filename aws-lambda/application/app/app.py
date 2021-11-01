import boto3
import json
from datetime import datetime

AWS_CLIENT_ID=""
AWS_CLIENT_SECRET=""
REGION_DEFAULT = "sa-east-1"
BUCKET_NAME = "bucket-teste"
ENDPOINT_URL_DEFAULT = "http://localhost:4566"
SQS_QUEUE_URL = f"{ENDPOINT_URL_DEFAULT}/000000000000/queue-teste"

def get_s3_client():
    return boto3.client('s3', aws_access_key_id=AWS_CLIENT_ID, aws_secret_access_key=AWS_CLIENT_SECRET, region_name=REGION_DEFAULT,
                        endpoint_url=ENDPOINT_URL_DEFAULT)
def get_sqs_client():
    return boto3.client('sqs', aws_access_key_id=AWS_CLIENT_ID, aws_secret_access_key=AWS_CLIENT_SECRET, region_name=REGION_DEFAULT,
                        endpoint_url=ENDPOINT_URL_DEFAULT)

def lambda_handler(event, context):
    # S3
    s3 = get_s3_client()
    response = s3.list_buckets()
    print('Listando buckets:')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')
    
    lista_arquivos = s3.list_objects(Bucket=BUCKET_NAME, MaxKeys=10)
    print("S3 - lista_arquivos:", lista_arquivos)
    object_arquivo_config = s3.get_object(Bucket=BUCKET_NAME, Key='config.json')
    file_content = object_arquivo_config['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print("S3 - config content:", json_content)
    
    # SQS
    sqs = get_sqs_client()
    # Enviando evento
    response = sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody='world')
    print("SQS - message id:", response.get('MessageId'))
    print("SQS - message body:", response.get('MD5OfMessageBody'))

    return f"Hello {event['name']}"

if __name__ == "__main__":
    lambda_handler({"name": "Marcelo"}, {})