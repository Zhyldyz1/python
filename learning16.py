import boto3

client = boto3.client('logs')
log_group = '/aws/lambda/my-function'

streams = client.describe_log_streams(logGroupName=log_group, orderBy='LastEventTime', descending=True)
stream_name = streams['logStreams'][0]['logStreamName']

events = client.get_log_events(logGroupName=log_group, logStreamName=stream_name)
for e in events['events']:
    print(e['timestamp'], e['message'])
