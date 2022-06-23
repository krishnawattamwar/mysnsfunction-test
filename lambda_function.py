import os
import boto3
import json

#print('Loading function')

def send_sns(message, subject):
    client = boto3.client("sns")
    topic_arn = os.environ["SNS_ARN"]
    response = client.publish(
        TopicArn=topic_arn, Message=message, Subject=subject)
    return response

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    msg = json.loads(message)
    print(msg)
    message= str("- Alarm Name: " + msg["AlarmName"] + "\n- Alarm Description: " + msg["AlarmDescription"] + "\n- Timestamp: " + msg["StateChangeTime"] + " UTC" + "\n- Threshold: " + msg["NewStateReason"])
    subject = str("ALARM: JuvYou-DevOps-Alert - " + msg["Region"])
    send_sns(message, subject)
#kri
