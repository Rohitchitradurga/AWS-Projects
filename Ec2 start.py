import boto3
import time
testing_instance_id = 'i-0a8dd282e182ef5cd'
testing_instance_id = False
def run():
    region = 'us-east-2'
    key_id = 'AKIAJBQ47KU6QKBHIVMA'
    access_key = '7QzUqtVU1yf82vyCOJ1SdhICVPriAC9OFIsZXqt7'
    ami_id = 'c77456a2'
    # Security Group ID
    sg_id = 'c77456a2'
    instance_type = 't2.micro'
    subnet_id = 'c57dc4ac'
    InstanceInitiatedShutdownBehavior = 'stop'

    newInstancesList=[]
    
    min_count = 20
    max_count = 21

    NetworkIface = [
        {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId': subnet_id,
            'Groups': [
                sg_id
            ]
        }
    ]

    ec2Instance = boto3.resource('ec2', region_name=region, aws_access_key_id=key_id, aws_secret_access_key=access_key)

    for num in range(min_count,max_count):
        TagSpecifications = [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Rohit' + str(num)
                    },
                    {
                        'Key': 'Service',
                        'Value': 'Testing'
                    },
                ]
            },
        ]
        
        if not testing_instance_id:
            newInstance = ec2Instance.create_instances(DryRun=False,
                                        ImageId=ami_id, 
                                        InstanceType=instance_type, 
                                        MinCount=1, 
                                        MaxCount=1,
                                        InstanceInitiatedShutdownBehavior=InstanceInitiatedShutdownBehavior,
                                        TagSpecifications=TagSpecifications, 
                                        NetworkInterfaces=NetworkIface)
            k = newInstance.pop()
            instance_id = k.id
            print(instance_id)
            time.sleep(2)
        else:
            instance_id = testing_instance_id
        
        instance = ec2Instance.Instance(instance_id)
        tempInst = {'id' : instance_id, 'ip' : instance.private_ip_address, 'name' : 'Rohit' + str(num) }
        print(newInstancesList.append( tempInst ))


if __name__ == '__main__':
    run()