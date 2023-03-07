# CloudTrail Event Monitor

## Description

This Python script checks CloudTrail events for all IAM users on AWS and displays the 5 latest events for each user in a nice format. The script also waits for 1 minute before checking again to avoid spamming the AWS API. The script is configured to only look for events in the last hour.

## Instructions:

1. Make sure you have the AWS CLI and Python installed on your local machine.
2. Configure the AWS CLI with your AWS access keys by running aws configure.
3. Install the Boto3 Python library by running pip install boto3.
4. Download the cloudtrail_event_monitor.py script and save it to a directory on your local machine.
5. Open a terminal window and navigate to the directory where the script is saved.
6. Run the script by running python cloudtrail_event_monitor.py.

Note: The script will run continuously until you manually stop it by pressing CTRL+C in the terminal window.
