#!/bin/bash
set -x
# Cria o bucket
awslocal dynamodb create-table \
    --table-name Stock \
    --attribute-definitions \
        AttributeName=Symbol,AttributeType=S \
        AttributeName=Description,AttributeType=S \
    --key-schema \
        AttributeName=Symbol,KeyType=HASH \
        AttributeName=Description,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
set +x