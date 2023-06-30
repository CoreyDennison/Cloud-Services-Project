import boto3


# Connect to EC2
ec2 = boto3.client("ec2")
# Get resources from EC2
ec2_resource = boto3.resource('ec2')
# Create variable with all instances and their  details
instances = ec2_resource.instances.all()

# instance id
instance_id = 'i-014035f4234432adb' 

# Describe the  instance
response = ec2.describe_instances(
            InstanceIds=[
                        instance_id,
                            ], 
            )
print(f"\nDescription of instance {instance_id}: \n {response} \n")

# Loop through all the instances and details
for instance in instances:
 # If the instance is running, stop it
    if instance.state['Name'] == 'running':
        print(f"The instance {instance_id} is running.\nStopping instance...")
        ec2.stop_instances(
            InstanceIds=[
                instance_id,
                    ],
                )
    print(f"The instance {instance_id} has been stopped.\n")

response = ec2.create_volume(
    AvailabilityZone='us-east-1d',
    Size=10,
    Iops=3000,
    VolumeType='gp3',
    TagSpecifications=[
        {
            'ResourceType':'volume',
            'Tags':[
                { 
                 'Key':'Boto3',                                                                                                                           'Value':'Volume',                                                                                                     
                },
            ]
        },
    ],
)

print(f"Creating volume...\n{response}\n")

#get all volumes from EC2
ec2_volumes = ec2_resource.volumes.all()
# Print volumes
print(f"Volumes:")
for volume in ec2_volumes:
    print(volume.id)