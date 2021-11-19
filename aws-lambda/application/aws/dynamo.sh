#!/bin/bash
set -x
# Cria o bucket
awslocal dynamodb --endpoint-url=http://localstack:4566 -- create-table \
    --table-name StockSymbols \
    --attribute-definitions \
        AttributeName=Symbol,AttributeType=S \
        AttributeName=Description,AttributeType=S \
    --key-schema \
        AttributeName=Symbol,KeyType=HASH \
        AttributeName=Description,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5

set +x