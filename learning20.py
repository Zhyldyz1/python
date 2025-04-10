import boto3
from datetime import datetime, timedelta

# Create AWS clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

# Get all running EC2 instances
def get_running_instances():
    instances = []
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                name = 'Unnamed'
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name':
                            name = tag['Value']
                instances.append({'InstanceId': instance['InstanceId'], 'Name': name})
    return instances

# Check if instance has low CPU usage
def is_low_cpu(instance_id):
    end = datetime.utcnow()
    start = end - timedelta(hours=6)

    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start,
        EndTime=end,
        Period=3600,
        Statistics=['Average']
    )

    datapoints = metrics.get('Datapoints', [])
    if not datapoints:
        return False

    avg_cpu = sum(point['Average'] for point in datapoints) / len(datapoints)
    return avg_cpu < 1

# Main logic
def main():
    instances = get_running_instances()
    for inst in instances:
        if is_low_cpu(inst['InstanceId']):
            print(f"Idle instance found: {inst['Name']} ({inst['InstanceId']})")

if __name__ == "__main__":
    main()
