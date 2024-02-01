# Global databases for storing event data

import datetime

events_db = {}  # Stores event details
attendees_db = {}  # Stores feedback for each event
loyalty_points_db = {} # Stores loyalty points for each attendee

# Function to create a new event
def create_event(event_id, name, speaker, date, capacity):
    # Check if event already exists to avoid duplication
    if event_id in events_db:
        print("Event ID already exists.")
        return False

    # Validate date format (YYYY-MM-DD)
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return False


    # Add new event to the database
    events_db[event_id] = {
        "name": name,
        "speaker": speaker,
        "date": date, # Use the original date string as it's now validated
        "capacity": capacity,
        "attendees": []
    }
    print("Event created successfully.")
    print("---------------------------------------")
    return True

# Function to modify an existing event
def modify_event(event_id, **kwargs):
    # Check if the event exists
    if event_id not in events_db:
        print("Event ID does not exist.")
        return False
    # Update event details based on provided arguments
    for key, value in kwargs.items():
        if key in events_db[event_id]:
            events_db[event_id][key] = value
        else:
            print(f"Invalid attribute: {key}")
    print("Event modified successfully.")
    print("---------------------------------------")
    return True

# Function to register an attendee for an event
def register_for_event(event_id, attendee_name):
    # Check if the event exists
    if event_id not in events_db:
        print("Event ID does not exist.")
        return False
    # Check if the event has reached its capacity
    if len(events_db[event_id]["attendees"]) >= events_db[event_id]["capacity"]:
        print("Event is full.")
        return False
    # Register the attendee and update loyalty points
    events_db[event_id]["attendees"].append(attendee_name)
    update_loyalty_points(attendee_name) # Update loyalty points after successful registration
    print(f"{attendee_name} registered successfully.")
    print("---------------------------------------")
    return True

# Function to collect feedback for an event
def collect_feedback(event_id, attendee_name, feedback):
    # Check if the event exists in the database
    if event_id not in events_db:
        print("Event ID does not exist.")
        print("---------------------------------------")
        return
    
    # Check if the attendee is registered for the event
    if attendee_name not in events_db[event_id]["attendees"]:
        print(f"This customer ({attendee_name}) is not registered for the event and cannot leave feedback.")
        print("---------------------------------------")
        return

    # Check if a sub-dictionary for the event exists in the feedback database; if not, create it
    if event_id not in attendees_db:
        attendees_db[event_id] = {}
    
    # Store the feedback
    attendees_db[event_id][attendee_name] = feedback
    print("Feedback received. Thank you!")
    print("---------------------------------------")

    

# Function to update loyalty points for an attendee
def update_loyalty_points(attendee_name):
    # Add points for attendance; if attendee is new, initialize with 10 points
    if attendee_name in loyalty_points_db:
        loyalty_points_db[attendee_name] += 10 #earn 10 points per event:
    else:
        loyalty_points_db[attendee_name] = 10
    print(f"{attendee_name} has earned 10 loyalty points.")
    print("---------------------------------------")

# Function to display loyalty points for a specific attendee
def display_loyalty_points(attendee_name):
    points = loyalty_points_db.get(attendee_name, 0)
    print(f"{attendee_name} has {points} loyalty points.")
    print("---------------------------------------")


# Function to generate a report on event attendance
def generate_event_attendance_report(event_id):
    # Check if the event exists
    if event_id not in events_db:
        print("Event ID does not exist.")
        return
    event = events_db[event_id]
    print(f"Attendance Report for {event['name']} ({event_id}):")
    # Print the list of attendees
    print(f"Total Attendees: {len(event['attendees'])}")
    if event['attendees']:
        print("List of Attendees:")
        for attendee in event['attendees']:
            print(f" - {attendee}")
    else:
        print("No attendees registered for this event.")
    print("---------------------------------------")

# Function to generate a report on loyalty points for all attendees
def generate_loyalty_points_report():
    if not loyalty_points_db:
        print("No loyalty points data available.")
        return
    print("Loyalty Points Report:")
    # Print loyalty points for each attendee
    for attendee, points in loyalty_points_db.items():
        print(f"{attendee}: {points} points")

# Function to generate a report on feedback for a specific event
def generate_event_feedback_report(event_id):
    if event_id not in attendees_db or not attendees_db[event_id]:
        print("No feedback available for this event.")
        return
    print(f"Feedback Report for Event ID {event_id}:")
    
    # Print feedback given by each attendee
    for attendee, feedback in attendees_db[event_id].items():
        print(f"{attendee}: {feedback}")

# User interface to interact with the event management system
def run_event_management_system():
    # Display options to the user
    while True:
        print("\nEvent Management System")
        print("1. Create Event")
        print("2. Modify Event")
        print("3. Register for Event")
        print("4. Collect Feedback")
        print("5. Generate Event Attendance Report")
        print("6. Generate Loyalty Points Report")
        print("7. Generate Event Feedback Report")
        print("8. Exit")
        print("---------------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            event_id = input("Enter event ID: ")
            name = input("Enter event name: ")
            speaker = input("Enter speaker name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            capacity = input("Enter event capacity: ")
            try:
                capacity = int(capacity)
                create_event(event_id, name, speaker, date, capacity)
            except ValueError:
                print("Invalid capacity. Please enter a number.")
            
        elif choice == "2":
            event_id = input("Enter event ID to modify: ")
            print("Enter new details (leave blank if no change):")
            name = input("New event name: ")
            speaker = input("New speaker name: ")
            date = input("New event date (YYYY-MM-DD): ")
            capacity = input("New event capacity: ")
            kwargs = {}
            if name: kwargs['name'] = name
            if speaker: kwargs['speaker'] = speaker
            if date: kwargs['date'] = date
            if capacity:
                try:
                    kwargs['capacity'] = int(capacity)
                except ValueError:
                    print("Invalid capacity. Please enter a number.")
            modify_event(event_id, **kwargs)

        elif choice == "3":
            event_id = input("Enter event ID to register: ")
            attendee_name = input("Enter your name: ")
            register_for_event(event_id, attendee_name)

        elif choice == "4":
            event_id = input("Enter event ID for feedback: ")
            attendee_name = input("Enter your name: ")
            feedback = input("Enter your feedback: ")
            collect_feedback(event_id, attendee_name, feedback)

        elif choice == "5":
            event_id = input("Enter event ID for the attendance report: ")
            generate_event_attendance_report(event_id)

        elif choice == "6":
            generate_loyalty_points_report()

        elif choice == "7":
            event_id = input("Enter event ID for the feedback report: ")
            generate_event_feedback_report(event_id)

        elif choice == "8":
            print("Exiting the Event Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Starting the system
run_event_management_system()

# Assuming the user chooses option 1 to create an event
# Then inputs the following:
# Enter event ID: EVT1001
# Enter event name: Tech Talk
# Enter speaker name: John Doe
# Enter event date (YYYY-MM-DD): 2024-02-15
# Enter event capacity: 50

# Assuming the user chooses option 2 to modify an event
# Then inputs the following:
# Enter event ID to register: EVT1001
# Enter your name: Alice


# Assuming the user chooses option 3 to register for an event
# Then inputs the following:
# Enter event ID to register: EVT1001
# Enter your name: Alice

# Assuming the user chooses option 4 to collect feedback
# Then inputs the following:
# Enter event ID for feedback: EVT1001
# Enter your name: Alice
# Enter your feedback: Great event, very informative!

# Assuming the user chooses option 5 to generate a report
# Then inputs the following:
# Enter event ID for report: EVT1001

# Finally, the user chooses option 6 to exit the system
