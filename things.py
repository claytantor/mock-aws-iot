import boto3
import sys
import argparse
import json

boto3.set_stream_logger(name='botocore')
client = boto3.client('iot')

def list_things():
    response = client.list_things()
    print(response)

def create_thing(thing_name):
    response = client.create_thing(
        thingName=thing_name,
        thingTypeName='RaspberryPi',
        attributePayload={
            'attributes': {
                'foo': 'bar'
            }
        }
    )
    print(response)    

def describe_endpoint():
    response = client.describe_endpoint(
        endpointType='iot:Data-ATS'
    )
    print(response)  

def keys_and_cert():
    response = client.create_keys_and_certificate(
        setAsActive=True
    )
    print(response)  

def attach_thing_principal(thing_name):
    response = client.attach_thing_principal(
        thingName=thing_name,
        principal='arn:aws:iot:us-east-1:705212546939:cert/4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b'
    )
    print(response)  

def create_policy(thing_name, policy_model_file):
    data = "{}"
    with open(policy_model_file, 'r') as file:
        data = file.read().replace('\n', '')
    response = client.create_policy(
        policyName='policy-{0}'.format(thing_name),
        policyDocument=data
    )
    print(response)

def attach_policy(thing_name):
    print('policy-{0}'.format(thing_name))
    response = client.attach_policy(
        policyName='policy-{0}'.format(thing_name),
        target='arn:aws:iot:us-east-1:705212546939:cert/4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b'
    )
    print(response)

def detach_policy(thing_name):
    print('policy-{0}'.format(thing_name))
    response = client.detach_policy(
        policyName='policy-{0}'.format(thing_name),
        target='arn:aws:iot:us-east-1:705212546939:cert/4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b'
    )
    print(response)


# console.log("========== detachThingPrincipal ==============");
# return detachThingPrincipal(
#     results.thing.thingName, results.thing.certificateArn, callback); 
def detach_thing_principal(thing_name):
    response = client.detach_thing_principal(
        thingName=thing_name,
        principal='arn:aws:iot:us-east-1:705212546939:cert/4d26e45bd8b72eecf9288a62c266af7ea7ad5e243c92d5736268d6eb0a17805b'
    )
    print(response)

def main():
    # print command line arguments
    parser = argparse.ArgumentParser(description='Get shadow logging for a thing.')
    parser.add_argument('--method', help='method to run')
    parser.add_argument('--name', help='name of thing')
    parser.add_argument('--file', help='name of thing')

    args = parser.parse_args()
    if args.method == 'list_things':
        list_things()
    if args.method == 'create_thing':
        create_thing(args.name)
    if args.method == 'describe_endpoint':
        describe_endpoint()
    if args.method == 'keys_and_cert':
        keys_and_cert()
    if args.method == 'attach_thing_principal':
        attach_thing_principal(args.name)
    if args.method == 'create_policy':
        create_policy(args.name, args.file)
    if args.method == 'attach_policy':
        attach_policy(args.name)
    if args.method == 'detach_policy':
        detach_policy(args.name)
    if args.method == 'detach_policy':
        detach_policy(args.name)
    if args.method == 'detach_thing_principal':
        detach_thing_principal(args.name) 


if __name__ == "__main__":
    main()