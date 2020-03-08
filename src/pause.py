# Pause Service API endpoint (POST) -- https://<hostname>.execute-api.<region>.amazonaws.com/dev/pause?id=<routine_id> #

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Region to be changed accordingly #
table = dynamodb.Table('Routine_Service')

def lambda_handler(event, context):
	routine_id = event["id"]
	
	# Check if service exists #
	try:
		response = table.get_item(
			Key={
				"routine_id": routine_id
			}
		)
		
	except ClientError as e:
		print(e)
		return(e)
		
	else:
		# Pause the Service and update time if it exists else return error #
		if "Item" in response:
			try:
				item = table.update_item(
					Key={
						'routine_id': routine_id
					},
					UpdateExpression="set modifiedAt=:mt",
					ExpressionAttributeValues={
						':mt': datetime.now()
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
				print("Modified the service time successfully")
				return response
				
			except ClientError as e:
					print(e)
					return(e)
					
		else:
			return("Error")