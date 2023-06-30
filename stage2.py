import boto3


# Connect to EC2
ec2 = boto3.client("ec2")
# Get resources from EC2
ec2_resource = boto3.resource('ec2')
# Create variable with all instances and their  details
instances = ec2_resource.instances.all()
#Create variable with all EC2 volumes
ec2_volumes = ec2_resource.volumes.all()

#instance id
instance_id = 'i-014035f4234432adb' 

# Print all volumes
print('Volumes:')
for volume in ec2_volumes:
    print(volume.id)

#Get volume ID from volume size with a state of 'available'.
for volume in ec2_volumes:
    if volume.size == 10 and volume.state == 'available':
        new_volume_id = volume.id
print(f"The new volume's ID is {new_volume_id}")

response = ec2.attach_volume(
    Device='/dev/sdf',
    InstanceId=instance_id,
    VolumeId=new_volume_id,
)

print(f"Attaching volume {new_volume_id} to instance {instance_id}...\n{response}\n")

response = ec2.describe_volumes(
)

print(f"Volume descriptions:\n{response}\n")

for instance in instances:
    if instance.state['Name'] == 'stopped':
        ec2.start_instances(
            InstanceIds=[
                    instance_id,
                ],
            )
    print(f"Starting instance {instance_id}.")