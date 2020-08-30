# zomentum_assignment
test assignment for campus hiring

# Problem Statement :
You have to design a REST interface for a movie theatre ticket booking system. It should support the following business cases:

1. An endpoint to book a ticket using a user’s name, phone number, and timings. /endl
2. An endpoint to update a ticket timing.
3. An endpoint to view all the tickets for a particular time.
4. An endpoint to delete a particular ticket.
5. An endpoint to view the user’s details based on the ticket id.
6. Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.
7. Note: For a particular timing, a maximum of 20 tickets can be booked.
8. You should follow the REST paradigm while building your application.
9. You can use any database you like.
10. Create a proper readme for your project.
11. Plus point if you could delete all the tickets which are expired automatically.
12. Plus point if you could write the tests for all the endpoints.
13. Please attach a screenshot of your postman while testing your application.
14. Please avoid plagiarism.


# Solution
## Technologies used:

1. django
2. django rest_framework
3. Database used : sqlite3
4. Postman for testing

## Ticket Schema
|Field|Type|Description|
|-----|----|-----------|
|Id|Primary Key|Uniqely Identify each ticket|
|Username|charfield(maxlen=50)|Name of the user|
|PhoneNo|charfield(maxlen=10)|Phone no of the user|
|timing|DateTimeField|timing of the ticket|
|booking_time|DatetimeField|time at which ticket is booked|
|is_expired|booleanFiled|Status of the ticket|

## Getting Started
After cloning the file run the following commands in the project folder

`pipenv shell` to activate the virtual environment

`pipenv install -r requirements.txt` to get the get libraries

`cd api` to get to the coerrect folder

`python manage.py runserver` to run the server 

## Routes for api:
```
Endpoint: http://127.0.0.1:8000/viewtiming/<time>
Method: GET
Input: time (yyyy-mm-ddThh:mm:ss) [hours in 24 hr format]
Output: No of Tickets available for particular time
```
```
Endpoint: http://127.0.0.1:8000/view/
Method: GET
Input:No input
Output: Details of all the tickets booked
```
```
Endpoint: http://127.0.0.1:8000/viewbyid/<ID>
Method: GET
Input: Unique Id of the booked ticket
Output: Details of Ticket with the ID
```
```
Endpoint: http://127.0.0.1:8000/bookticket/
Method: POST
Input:data= {
	  "UserName": "name",
          "PhoneNo": "phone Number",
          "timing": "timing (yyyy-mm-ddThh:mm:ss)"
      }
Output:  if successful : Details of the ticket booked otherwise { "status": "no tickets available"} 
```
```
Endpoint: http://127.0.0.1:8000/updateticket/<ID>
Method: PUT
Input: Unique Id of the booked ticket
      data ={ "timing" : "timing (yyyy-mm-ddThh:mm:ss)"}
Output: { "status" : "update succefull" }
```
```
Endpoint: http://127.0.0.1:8000/deleteticket/<ID>
Method: DELETE
Input: Unique Id of the booked ticket
Output: { "success": "delete successful" }
```
```
Endpoint: http://127.0.0.1:8000/viewbytime/<timings>
Method: GET
Input: timings (yyyy-mm-ddThh:mm:ss) [hours in 24 hr format]
Output: List of details of tickets booked for the given time 
```
```
Endpoint: http://127.0.0.1:8000/expire
Method: PUT
Input: No Input
Output: Update the is_expired field of tickets for timing 8 hours before the current timing 
```
```
Endpoint: http://127.0.0.1:8000/deleteexpired
Method: DELETE
Input: No Input
Output:  Delete all the tickets with is_expired field set to True
```

##ScreenShots

![imagename](1.check_no_of_ticks_avail_at_time.png)











