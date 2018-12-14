#!/bin/sh

set -e

zip -r9 step_to_stl_lambda.zip \
  aws_s3.py \
  conversion_error.py \
  handler.py \
  step_to_stl.py \
  volume.py \
  lib \
  OCC/*.py \
  OCC/*.so

echo "Package complete.  Uploading your function to AWS Lambda..."

aws lambda update-function-code --function-name engine --zip-file fileb://step_to_stl_lambda.zip --profile roundtable
