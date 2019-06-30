import json
from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route("/things")
def things():
    json_data = request.get_json()
    # print(request.__dict__)
    response = {'ResponseMetadata': {'RequestId': '29553f77-7b7a-11e9-90f8-4ba9184bac2b', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Tue, 21 May 2019 03:40:22 GMT', 'content-type': 'application/json', 'content-length': '364', 'connection': 'keep-alive', 'x-amzn-requestid': '29553f77-7b7a-11e9-90f8-4ba9184bac2b', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aA7t9EVmIAMF10w=', 'x-amzn-trace-id': 'Root=1-5ce37326-340796de33eae75ef28a3600'}, 'RetryAttempts': 0}, 'things': [{'thingName': 'ecd13b11-ubuntu-reedway', 'thingTypeName': 'RaspberryPi', 'thingArn': 'arn:aws:iot:us-east-1:705212546939:thing/ecd13b11-ubuntu-reedway', 'attributes': {}, 'version': 1}, {'thingName': 'ecd13b11-yazka', 'thingTypeName': 'RaspberryPi', 'thingArn': 'arn:aws:iot:us-east-1:705212546939:thing/ecd13b11-yazka', 'attributes': {}, 'version': 1}]}

    return jsonify(response)

@app.route('/things/<thing_id>', methods=['GET', 'POST', 'DELETE'])
def createThing(thing_id):

    if request.method == 'POST' or request.method == 'DELETE':      
        json_data = request.get_json()
        response = {'ResponseMetadata': {'RequestId': '3cbaf64d-7c34-11e9-8eaa-3f48b258e360', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 01:52:21 GMT', 'content-type': 'application/json', 'content-length': '151', 'connection': 'keep-alive', 'x-amzn-requestid': '3cbaf64d-7c34-11e9-8eaa-3f48b258e360', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aD-1SE_IIAMFyfQ=', 'x-amzn-trace-id': 'Root=1-5ce4ab55-e9ccef9425ecfea935c8e2b5'}, 'RetryAttempts': 0}, 'thingName': 'd3333b61-yaza32', 'thingArn': 'arn:aws:iot:us-east-1:705212546939:thing/d3333b61-yaza32', 'thingId': '5bb23190-5366-4b7f-9b93-3f7b8b980860'}

        return jsonify(response)

@app.route("/endpoint")
def endpoint():
    json_data = request.get_json()
    # print(request.__dict__)
    response = {'ResponseMetadata': {'RequestId': '45ad8a5d-7c36-11e9-a8a5-f5141da4598d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 02:06:55 GMT', 'content-type': 'application/json', 'content-length': '69', 'connection': 'keep-alive', 'x-amzn-requestid': '45ad8a5d-7c36-11e9-a8a5-f5141da4598d', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aEA92EFSIAMFa2A=', 'x-amzn-trace-id': 'Root=1-5ce4aebf-26fdfc575f21353fb8025fd6'}, 'RetryAttempts': 0}, 'endpointAddress': 'a1khvirpxw0646-ats.iot.us-east-1.amazonaws.com'}

    return jsonify(response)



@app.route('/keys-and-certificate', methods=['GET', 'POST'])
def keysAndCert():

    if request.method == 'POST':      
        json_data = request.get_json()

        response = {'ResponseMetadata': {'RequestId': '4f1b383c-7c37-11e9-8d96-b5d3d7ad446e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 02:14:20 GMT', 'content-type': 'application/json', 'content-length': '3678', 'connection': 'keep-alive', 'x-amzn-requestid': '4f1b383c-7c37-11e9-8d96-b5d3d7ad446e', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aECDbH_hIAMFS4A=', 'x-amzn-trace-id': 'Root=1-5ce4b07c-da8f218583bea6ba458131a7'}, 'RetryAttempts': 0}, 'certificateArn': 'arn:aws:iot:us-east-1:705212546939:cert/4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b', 'certificateId': '4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b', 'certificatePem': '-----BEGIN CERTIFICATE-----\nMIIDWjCCAkKgAwIBAgIVAKagvgMp2TprFvDpTdLGjm+8bT55MA0GCSqGSIb3DQEB\nCwUAME0xSzBJBgNVBAsMQkFtYXpvbiBXZWIgU2VydmljZXMgTz1BbWF6b24uY29t\nIEluYy4gTD1TZWF0dGxlIFNUPVdhc2hpbmd0b24gQz1VUzAeFw0xOTA1MjIwMjEy\nMjBaFw00OTEyMzEyMzU5NTlaMB4xHDAaBgNVBAMME0FXUyBJb1QgQ2VydGlmaWNh\ndGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCdkLr61xx5Arzd3Wtd\nEO5LViyqiYBnDs3RChU7dtsjHhVbTtpETKn3jx70/eB/CuOgFgLA2GXlNWBUPXVu\n10Tv5wx1itam+HJBi/WEUTqewZCweD1famDEP9jOXpZ8BI+0x5gg98ZN5xPc9sKu\nz25lZJ2ga8OLzCnCM9EXTmJf2bBW+f4+gS2pgi5Yv4c4jqnZf3LatiJjBzZQfwFo\n5SyNm/9V12+2Q6ygNX/sinQDbtyfNaULT0UG3bYtVzYPregm8uz7gXI3zDfgDHxy\nlwBponEZlAFNMqW2qj9EXPOxU8Fzbo3afUOxBvIr434EpRK4u5L/F3D00anqwApa\nZkabAgMBAAGjYDBeMB8GA1UdIwQYMBaAFOwjoZjNyw0wQhJSpciRl9JeMBhVMB0G\nA1UdDgQWBBSYy21m2ISPdhyR9ARNB2LK6xJ0tDAMBgNVHRMBAf8EAjAAMA4GA1Ud\nDwEB/wQEAwIHgDANBgkqhkiG9w0BAQsFAAOCAQEAkZoAyPgTfv+3Yclw0TfSOOPZ\n0Pjg+8m6o+7lstCJvH+E4Dyrbj+vNPQxAaEa3eYlfZXXI2LIVjIYt9c7HOhsgPSS\nBXNEmXqhuFvDyHdttz1/B/vWuCvtcuZ0uPRp6+tw1ucKQPDq/UqbjCuUd6QzgzL5\n+RVK1h/vTiGV7Q7VAjB5PovxLQSxJVepN6TTT5R18VdKInKCvHadSSpI7aqONReK\nuodwjN10QGxdbD5Pbrc8dtZZUS3X/dwiMAoUwNtnb233k2AbcSEO0LMl84ec/4UD\nJH/H9EdqO0gVsrkZQYoBiQW3v3hlH1tvyokyuYY6w9EkDey7GsZyzXRM+G8siQ==\n-----END CERTIFICATE-----\n', 'keyPair': {'PublicKey': '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnZC6+tcceQK83d1rXRDu\nS1YsqomAZw7N0QoVO3bbIx4VW07aREyp948e9P3gfwrjoBYCwNhl5TVgVD11btdE\n7+cMdYrWpvhyQYv1hFE6nsGQsHg9X2pgxD/Yzl6WfASPtMeYIPfGTecT3PbCrs9u\nZWSdoGvDi8wpwjPRF05iX9mwVvn+PoEtqYIuWL+HOI6p2X9y2rYiYwc2UH8BaOUs\njZv/VddvtkOsoDV/7Ip0A27cnzWlC09FBt22LVc2D63oJvLs+4FyN8w34Ax8cpcA\naaJxGZQBTTKltqo/RFzzsVPBc26N2n1DsQbyK+N+BKUSuLuS/xdw9NGp6sAKWmZG\nmwIDAQAB\n-----END PUBLIC KEY-----\n', 'PrivateKey': '-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAnZC6+tcceQK83d1rXRDuS1YsqomAZw7N0QoVO3bbIx4VW07a\nREyp948e9P3gfwrjoBYCwNhl5TVgVD11btdE7+cMdYrWpvhyQYv1hFE6nsGQsHg9\nX2pgxD/Yzl6WfASPtMeYIPfGTecT3PbCrs9uZWSdoGvDi8wpwjPRF05iX9mwVvn+\nPoEtqYIuWL+HOI6p2X9y2rYiYwc2UH8BaOUsjZv/VddvtkOsoDV/7Ip0A27cnzWl\nC09FBt22LVc2D63oJvLs+4FyN8w34Ax8cpcAaaJxGZQBTTKltqo/RFzzsVPBc26N\n2n1DsQbyK+N+BKUSuLuS/xdw9NGp6sAKWmZGmwIDAQABAoIBAAry5atMi1P1Vr5s\nBmvfI0/k2xG2oE+I/dBKzRLmvW+BRaakohIg6aakMViA07rAPPUA0own/VyiCuGP\nq7taBhZNjdYVIblUhkv7t8HMCzDA7pb0o/8fWz4H2b7tX7OadYnwXKfdz8/WANFX\n7EtNarRs+28MTfhG5ZfzFdJyxe83C1d08sdn4TIPctRThhmZ443dyxdUkOLdu5NE\n5jwu1R0ddrp4hNXjdz0j+lNSPyktENJvISFRZogFNzgoFf3u6IdyhKRE2jeofaf+\nmpdqspiGpkIoWntHJc7Q0HWVxxDzYbsVrReMQ8jgkcRnodp/as4SvLqtahwjaAET\nKUatNzECgYEAzqYuAOU2zSyVHDBESEXIPJ4MjehLGp0a09Nzoq5CEJ+hlbaQ37rs\nSnDuCfH6CpqSH5ElJ9Iegf/KOUKvEn5xTJ5/2VmAkBHV7vqRZmCFp7N9m1wh0+nV\nkdPVHeT3EnGxpozrKD1TLwdabF0/GQM6r14gysF/qO8+qyOVAp5WBqUCgYEAwzG8\ndhPFyiydpXPJ7AZzY7CGENfneghVew3TaI/asDnVxQfDnz/LHySkeCeA3pe7dbDd\nIj5VFbH7W8kUZjyHAmKdWEhQV9UWBzX3D+LGd+XbJmsdJTOaLYWYH1OUY4MtenBF\njR635AeILAjNMQ5iyDsmfGJZVtTOr9N4P7uy1D8CgYAfibknpdPRSGaRYMRrC0te\nBPkBh1w++Y8omPLi9xlaFCLDCJPfsVVynv2VQvrYN3Lpoms7QpQpXvJr/sNdXTLJ\ncL8uWryGQFKYIGGkcEK1r20SEuOOxfc0RFIYN+OFSxjDxGn3QDS7zrF8LFb+6EFC\nlmkGyLVFAQ5dbBbHyYZziQKBgDzjF9GRS2JMVoSUwMjSHk5bcwZwArGrRdbTsj1s\nmh/cepUyXdAgGyFE0dT1JZrJo90LZX9YCDxzP2AbMjTN7qNM1Z4DOKSdQHjRWZbn\n+1bNKXYrdXT0SsSmZpRnAuOjuJz3xopFqcEEpHJv8Gm7/g5NfSzRlOKkETEBewIO\nb7MLAoGAPpOqIH544WkkviA2nta5G7JhqeBPuk+v/+m4d93z83vOlP+76t8uU6UM\nfWsr7ccxdGRa9SzEbscludWjA8JDxV1EEpgMHaV+DDWO/C7ZM5wnw7+Rwtcii70Z\nIivkwtBRZcAICtDYL4dQplYFeJ2WAWDAWtmiCU/IFBExR4QKhgo=\n-----END RSA PRIVATE KEY-----\n'}}

        return jsonify(response)

@app.route('/things/<thing_id>/principals', methods=['PUT', 'DELETE'])
def attachPrincipals(thing_id):

    if request.method == 'PUT':      
        json_data = request.get_json()

        response = {'ResponseMetadata': {'RequestId': 'a584629d-7c38-11e9-9683-6f0b02608d20', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 02:23:54 GMT', 'content-type': 'application/json', 'content-length': '3', 'connection': 'keep-alive', 'x-amzn-requestid': 'a584629d-7c38-11e9-9683-6f0b02608d20', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aEDdMHNIoAMF9Dg=', 'x-amzn-trace-id': 'Root=1-5ce4b2ba-f77093069f07eea01281e867'}, 'RetryAttempts': 0}}

        return jsonify(response)

    if request.method == 'DELETE':      
        json_data = request.get_json()

        response = {'ResponseMetadata': {'RequestId': '1f116d96-7ced-11e9-9e35-87536de318ca', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 23:55:48 GMT', 'content-type': 'application/json', 'content-length': '3', 'connection': 'keep-alive', 'x-amzn-requestid': '1f116d96-7ced-11e9-9e35-87536de318ca', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aHAspEDBoAMF7eQ=', 'x-amzn-trace-id': 'Root=1-5ce5e184-c93f5e60e2c38e1c7dc907c0'}, 'RetryAttempts': 0}}

        return jsonify(response)

# "POST /policies/policy-d3333b61-yaza32
@app.route('/policies/<thing_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def createPolicy(thing_id):
    if request.method == 'POST':      
        json_data = request.get_json()

        response = {'ResponseMetadata': {'RequestId': '2c3f0ee3-7c3d-11e9-804d-c7387fb1165c', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 02:56:18 GMT', 'content-type': 'application/json', 'content-length': '1507', 'connection': 'keep-alive', 'x-amzn-requestid': '2c3f0ee3-7c3d-11e9-804d-c7387fb1165c', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aEIM8GqsoAMFrzg=', 'x-amzn-trace-id': 'Root=1-5ce4ba52-fa3836a8f5564fc6eb2fa626'}, 'RetryAttempts': 0}, 'policyName': 'policy-d3333b61-yaza32', 'policyArn': 'arn:aws:iot:us-east-1:705212546939:policy/policy-d3333b61-yaza32', 'policyDocument': '{    "Version": "2012-10-17",    "Statement": [        {            "Effect": "Allow",            "Action": [                "iot:Publish",                "iot:Receive"            ],            "Resource": [                "arn:aws:iot:us-east-1:undefined:topic/ingress/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:topic/egress/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:topic/pubsub/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:topic/flashlex/test"            ]        },        {            "Effect": "Allow",            "Action": [                "iot:Subscribe",                "iot:Receive"            ],            "Resource": [                "arn:aws:iot:us-east-1:undefined:topicfilter/ingress/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:topicfilter/egress/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:topicfilter/pubsub/d3333b61-yaza32"            ]        },        {            "Effect": "Allow",            "Action": [                "iot:Connect"            ],            "Resource": [                "arn:aws:iot:us-east-1:undefined:client/d3333b61-yaza32",                "arn:aws:iot:us-east-1:undefined:client/d3333b61-yaza32-backend"            ]        }    ]}', 'policyVersionId': '1'}

        return jsonify(response)

    if request.method == 'DELETE':  
        response = {'ResponseMetadata': {'RequestId': '58f8f73b-7ca5-11e9-9bfe-57a89e04eaed', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 15:22:01 GMT', 'content-type': 'application/json', 'content-length': '0', 'connection': 'keep-alive', 'x-amzn-requestid': '58f8f73b-7ca5-11e9-9bfe-57a89e04ebed', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aF1b_HwAIAMFvQw=', 'x-amzn-trace-id': 'Root=1-5ce56919-816394585344d29047fe8bc8'}, 'RetryAttempts': 0}}
        return jsonify(response)             

# PUT /target-policies/policy-d3333b61-yaza32
@app.route('/target-policies/<policy_id>', methods=['GET', 'POST', 'PUT'])
def attachPolicy(policy_id):
    json_data = request.get_json()    
    if request.method == 'PUT':      
        response = {'ResponseMetadata': {'RequestId': '51c82054-7c3d-11e9-bf41-3df4f154f949', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 02:57:21 GMT', 'content-type': 'application/json', 'content-length': '0', 'connection': 'keep-alive', 'x-amzn-requestid': '51c82054-7c3d-11e9-bf41-3df4f154f949', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aEIWyEczIAMF9-w=', 'x-amzn-trace-id': 'Root=1-5ce4ba91-e32f4fe4bbd8715ce077de8d'}, 'RetryAttempts': 0}}
        return jsonify(response)

    if request.method == 'POST':
        response = {'ResponseMetadata': {'RequestId': '58f8f73b-7ca5-11e9-9bfe-57a89e04ebed', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 15:22:01 GMT', 'content-type': 'application/json', 'content-length': '0', 'connection': 'keep-alive', 'x-amzn-requestid': '58f8f73b-7ca5-11e9-9bfe-57a89e04ebed', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aF1b_HwAIAMFvQw=', 'x-amzn-trace-id': 'Root=1-5ce56919-816394585344d29047fe8bc8'}, 'RetryAttempts': 0}}
        return jsonify(response)      

@app.route('/certificates/<cert_id>', methods=['PUT','DELETE'])
def inactivateCert(cert_id):    
    json_data = request.get_json()    
    if request.method == 'PUT' or request.method == 'DELETE' :      
        response = {'ResponseMetadata': {'RequestId': '58f8f73b-7ca5-11e9-9bfe-57a89e04eaed', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Wed, 22 May 2019 15:22:01 GMT', 'content-type': 'application/json', 'content-length': '0', 'connection': 'keep-alive', 'x-amzn-requestid': '58f8f73b-7ca5-11e9-9bfe-57a89e04ebed', 'access-control-allow-origin': '*', 'x-amz-apigw-id': 'aF1b_HwAIAMFvQw=', 'x-amzn-trace-id': 'Root=1-5ce56919-816394585344d29047fe8bc8'}, 'RetryAttempts': 0}}
        return jsonify(response) 


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')