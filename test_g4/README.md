# Project 5: E-Business Event Management System 


## What's the first version have

### Create Event
	- Create a dictionary data type
 	- For storing details of each event
  	- Value: eventID/name/speaker/date/capacity/attendees
### Modify Event
 	- For altering details of each event
### Register for Event
	- Attendees can register for events
 	- Capacity check to prevent overbooking
  	- In every event registration attendees will get loyalty 10 points
### Collect Feedback
	- Post-event feedback
### Generate Event Attendance Report
	- For reporting the attendees for each event
### Generate Loyalty Points Report
	- For reporting the loyalty points by attendees
### Generate Event Feedback Report
	- For reporting the feedback collected from attendees bu eventID
### Exit
	- close the program

## *!!!After the test, some of these functions need to be enhanced* ##

### collect_feedback (edited 01/02/2024 merged to main)
	- Add event existence check
  	- Attendee Registration Check
   *Create a new branch to modify ‘collect_feedback’ function.*
1. Adding Event Existence Check: Firstly, the function checks if the provided event_id exists within the events_db. If it doesn't, it prints a message stating that the event ID does not exist and returns without executing further.
2. Attendee Registration Check: Before accepting feedback, the function verifies if the attendee (identified by attendee_name) is registered for the specified event by checking their presence in the event's attendees list. If the attendee is not found, a message is printed indicating that the customer does not exist in the event's records, and the function returns without collecting feedback.
3. Feedback Collection: If the attendee is found, the function proceeds to collect their feedback. It checks if there's an existing feedback entry for the event in attendees_db; if not, it creates one. Then, it stores the attendee's feedback.
   	
### Date and time 
	- At first, just allows the user to input a number that has a pattern in the placeholder (Enter event date (YYYY-MM-DD):)
 	- Need date format validation

       
