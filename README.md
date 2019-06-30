# aws-iot-shadow
shadows and mocks for flashlex iot testing

## creating the virtualenv
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## shadows
`python thing.py --method list_things`

## mocks

```bash
docker build -t mock-aws-iot:latest .
sudo docker run -d -p 5000:5000 mock-aws-iot:latest
aws --endpoint-url=http://127.0.0.1:5000 --no-verify-ssl --region=us-east-1 iot list-things
```
and the response:

```
2019-05-20 21:34:54,957 botocore.retryhandler [DEBUG] No retry needed.
{'ResponseMetadata': {'RequestId': 'c832a2e7-7b81-11e9-a736-f3743e641bb0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Tue, 21 May 2019 04:34:55 GMT', 'content-type': 'application/json', 'content-length': '364', 'connection': 'keep-alive', 'x-amzn-requestid': 'c832a2e7-7b81-11e9-a736-f3743e641bb0', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aBDtXEHQIAMFV7Q=', 'x-amzn-trace-id': 'Root=1-5ce37fef-b205c2c6eba3262659dcd384'}, 'RetryAttempts': 0}, 'things': [{'thingName': 'ecd13b11-ubuntu-reedway', 'thingTypeName': 'RaspberryPi', 'thingArn': 'arn:aws:iot:us-east-1:705212546939:thing/ecd13b11-ubuntu-reedway', 'attributes': {}, 'version': 1}, {'thingName': 'ecd13b11-yazka', 'thingTypeName': 'RaspberryPi', 'thingArn': 'arn:aws:iot:us-east-1:705212546939:thing/ecd13b11-yazka', 'attributes': {}, 'version': 1}]}
```