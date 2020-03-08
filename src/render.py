# Render HTML page API endpoint (GET) -- https://<hostname>.execute-api.<region>.amazonaws.com/dev/render #

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import uuid
from datetime import datetime
from json2html import * # library to convert json object to HMTL tabular format #

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Region to be changed accordingly #
table = dynamodb.Table('Routine_Service')

def lambda_handler(event, context):
	# Scan all the service ids #
	try:
		response = table.scan()
		if "Items" in response:
			# Convert JSON obj to HTML tabular form #
			json_data = response["Items"]
			json_obj_in_html = json2html.convert(json = json_data)
			print(json_obj_in_html)
			return(json_obj_in_html)
			
		else:
			print("No data")
			return("No data")
			
	except ClientError as e:
		print(e)
		return(e)