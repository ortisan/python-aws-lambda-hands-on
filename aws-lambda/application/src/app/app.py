import json


def lambda_handler(event, context):
    return f"Hello {event['name']}"
