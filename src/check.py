# Check Service API endpoint (GET) -- https://<hostname>.execute-api.<region>.amazonaws.com/dev/check?id=<routine_id> #

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Region to be changed accordingly #
table = dynamodb.Table('Routine_Service')

def lambda_handler(event, context):
	# Check if unique id is given in API parameter else return data for all unique ids #
	if "id" in event:
		routine_id = event["id"]
	
		try:
			response = table.get_item(
				Key={
					"routine_id": routine_id
				}
			)

			stepTimeCount = response["Item"]["stepTimeCount"]
			creation_time = response["Item"]["creation_time"]
			steptime = response["Item"]["steptime"]
			return(stepTimeCount, creation_time, steptime)
			
		except ClientError as e:
			print(e)
			return(e)
				
	else:
		try:
			response = table.scan()
			for item in response["Items"]:
				stepTimeCount = item["stepTimeCount"]
				creation_time = item["creation_time"]
				steptime = item["steptime"]
				return(stepTimeCount, creation_time, steptime)
				
		except ClientError as e:
			print(e)
			return(e)