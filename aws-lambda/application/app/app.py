import boto3
import json
from datetime import datetime

REGION_DEFAULT = "sa-east-1"
BUCKET_NAME = "bucket-teste"
ENDPOINT_URL_DEFAULT = "http://localhost:4566"
SQS_QUEUE_URL = f"{ENDPOINT_URL_DEFAULT}/000000000000/queue-teste"

def get_s3_client():
    return boto3.client('s3', endpoint_url=ENDPOINT_URL_DEFAULT, region_name=REGION_DEFAULT)
def get_sqs_client():
    return boto3.client('sqs', endpoint_url=ENDPOINT_URL_DEFAULT, region_name=REGION_DEFAULT)
def get_dynamo_client():
    return boto3.client('dynamodb', endpoint_url=ENDPOINT_URL_DEFAULT, region_name=REGION_DEFAULT)

def lambda_handler(event, context):
    # S3
    print("### S3 DEMO")
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
    print("### SQS DEMO")
    sqs = get_sqs_client()
    # Enviando evento
    response = sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody='world')
    print("SQS - message id:", response.get('MessageId'))
    print("SQS - message body:", response.get('MD5OfMessageBody'))

    # DYNAMO
    print("### DYNAMO DEMO")
    dynamo = get_dynamo_client()
    # Lista de tabelas
    tables = dynamo.list_tables()
    print("Tables: ", tables)
    # Put Item
    dict = {
                'Symbol': {'S', 'BTC'},
                'Description': {'S', 'Bitcoin'}
            }

    item_inserted = dynamo.put_item(
        TableName='StockSymbols',
        Item = {
                'Symbol': {'S': 'BTC'},
                'Description': {'S': 'Bitcoin'}
            }
    )
    print("Item inserted:", item_inserted)

    item_filtered = dynamo.get_item(
        TableName='StockSymbols',
        Key = {
                'Symbol': {'S': 'BTC'},
                'Description': {'S': 'Bitcoin'}
            }
    )

    print("Item filtered:", item_filtered)

    return f"Hello {event['name']}"

if __name__ == "__main__":
    lambda_handler({"name": "Marcelo"}, {})