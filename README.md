# RSA - Routine Service Application

Overview:
------------------------------------------------------------------------------------

This application creates a new service routine by calculating every step time count with start value for each service. Application also has several features like to clear the service timer and set the status accordingly, pause the service and modify the time as well as rendering feature to fetch all the service details in an HTML page.

Overview of Workflows:
------------------------------------------------------------------------------------

1. Create a new service
    * Creates a new service routine with an unique identifier
    * Starts calculating every step time seconds depending on start value
    
2. Check service with service id passed
    * Retrieves the service details by matching service id passed by the user
    
3. Check service without the service id
    * Retrieves all the service details present in the system
    
4. Render service in HTML page
    * Retrieves all the service details from the database and displays as HTML page
    
5. Clear the service
    * Sets the service timer to 0 and sets the status to "Stopped" in database
    
6. Pause the service
    * Pauses a given service and modifies the time in database to reflect the API response
    
    
Project Structure:
--------------------------------------------------------------------------------------

1. _create.py_ -- Creates a new service routine with an unique identifier, Starts calculating every step time seconds depending on start value
2. _check.py_ -- Retrieves the service details by matching service id passed by the user else returns all the services in the system
3. _render.py_ -- Retrieves all the service details from the database and displays as HTML page
4. _clear.py_ -- Sets the service timer to 0 and sets the status to "Stopped" in database
5. _pause.py_ -- Pauses a given service and modifies the time in database to reflect the API response


Pre requisites:
---------------------------------------------------------------------------------------

* Python 3.x
* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB

REST API endpoints:
---------------------------------------------------------------------------------------

1. create -- https://(hostname).execute-api.<region>.amazonaws.com/dev/create (POST)
2. check -- https://(hostname).execute-api.<region>.amazonaws.com/dev/check?id=<routine_id> (GET)
3. clear -- https://(hostname).execute-api.<region>.amazonaws.com/dev/clear?id=<routine_id> (POST)
4. pause -- https://(hostname).execute-api.<region>.amazonaws.com/dev/pause?id=<routine_id> (POST)
5. render -- https://(hostname).execute-api.<region>.amazonaws.com/dev/render (GET)
  
  
DynamoDB table structure:
---------------------------------------------------------------------------------------

* Table Name - Routine_Service
* Primary Key - routine_id
* Attributes - stepTimeCount, startval, steptime, creation_time, service_status, modifiedAt
