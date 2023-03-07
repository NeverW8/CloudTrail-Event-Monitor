import boto3
import time
from datetime import datetime, timedelta

# Create CloudTrail and IAM clients
cloudtrail = boto3.client('cloudtrail')
iam = boto3.client('iam')

# Get list of IAM users
users = iam.list_users()

while True:
    # Calculate start and end time for the query (last hour)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=1)

    # Iterate through all IAM users
    for user in users['Users']:
        user_name = user['UserName']

        # Get the most recent 5 events for the user from CloudTrail
        events = cloudtrail.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'Username',
                    'AttributeValue': user_name
                },
            ],
            StartTime=start_time,
            EndTime=end_time,
            MaxResults=5,
        )

        # Print the events for the user in a nice format
        print(f"Recent events for {user_name}:")
        for event in events['Events']:
            print(f"\tEvent Name: {event['EventName']}")
            print(f"\tEvent Time: {event['EventTime']}")
            print(f"\tEvent Source: {event['EventSource']}")
            print()

    # Wait for 1 minute before checking again
    time.sleep(60)
