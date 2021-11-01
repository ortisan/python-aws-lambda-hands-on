#!/bin/bash
set -x
# Cria o bucket
awslocal s3 mb s3://bucket-teste
# Copia o arquivo para o bucket
awslocal s3 cp /docker-entrypoint-initaws.d/config.json s3://bucket-teste/config.json
set +x