# Clear timer API endpoint (POST) -- https://<hostname>.execute-api.<region>.amazonaws.com/dev/clear?id=<routine_id> #

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Region to be changed accordingly #
table = dynamodb.Table('Routine_Service')

def lambda_handler(event, context):
	# Clear the timer if service exists else return error #
	if "id" in event:
		routine_id = event["id"]
		
		try:
			item = table.update_item(
				Key={
					'routine_id': routine_id
				},
				UpdateExpression="set stepTimeCount=:st, service_status=:sc",
				ExpressionAttributeValues={
					':st': 0,
					':sc': "Stopped"
				},
				ReturnValues="UPDATED_NEW"
			)
			response = {
				"statusCode": 200,
				"body": json.dumps(item),
				"headers": {
				  "Access-Control-Allow-Origin": "*",
				  "Access-Control-Allow-Credentials": "true"
					
				}
				
			}
			print("Cleared the service timer and updated status successfully")
			return response
			
		except ClientError as e:
				print(e)
				return(e)
				
	else:
		return("Error")
