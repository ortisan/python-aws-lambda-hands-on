#!/bin/bash
set -x
# Cria o SQS
awslocal sqs create-queue --endpoint-url=http://localstack:4566 --queue-name queue-teste --region=sa-east-1
set +x