# code_repository :stuck_out_tongue_winking_eye:

## In-class exercises and extra work for practicing.

- Collected into folder
- Modify some functions from Python test on 30/01/2024

# **_Week 1_**

## :running: Assessment

### :pencil2: Programming Test 20%

### :computer: Assignment 70%

### :open_file_folder: Code Repository 10%

    Code Repository- progress from week1 to week4
    Languages that we have to learn in this module
      - Python
      - Html
      - CSS
      - SqlLite
      - And other frameworks, Flask and Bootstrap
    Concept OOP (object-oriented programming)

## :round_pushpin: useful link

- [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Python Tutorial - W3 School](https://www.w3schools.com/python/default.asp)
- [Visual Studio Installation](https://code.visualstudio.com/)

# **_Week 2_**

### :blue_book: HTML and CSS

### :gem: GitHub - Version control software//save your progrress - Git is a memory card for code.

## :round_pushpin: useful link

- [Jordan's GitHub](<https://www.example.com](https://github.com/Jordan-Bruno/DDP2324-GitHubExercise)https://github.com/Jordan-Bruno/DDP2324-GitHubExercise>)
- [Bootstrap Theme](https://themes.getbootstrap.com/)
- [Bulma Responsive UI](https://bulma.io/alternative-to-bootstrap/)
- [HTML - W3 School](https://www.w3schools.com/html/html5_semantic_elements.asp)
- [How to connect VSCode to GitHub](https://code.visualstudio.com/docs/sourcecontrol/github)
- [Username config on VSCode](https://www.youtube.com/watch?v=c-arYUBnHhk)

# **_Week 3_**

### :chart_with_upwards_trend: SDLC Database

### :bookmark: Web Frameworks Dynamic Control

## :round_pushpin: useful link

- [Creating Relation Diagram](https://app.diagrams.net)
- [CSS Zen Garden](https://csszengarden.com/pages/alldesigns/)
- [Duncan's A mock shopping app demonstrating Flask and SQL usage.](https://github.com/DuncanJF/BuyBestBrands/tree/main)

# **_Week 4_**

### Flask environment setup by Duncan

## :round_pushpin: useful link

- [BuyBestBrand Project](https://github.com/DuncanJF/BuyBestBrands/tree/main)

---

# Project 5: E-Business Event Management System

## What are the first version had

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

## _!!!After the test, some of these functions need to be enhanced_

### collect_feedback (edited 01/02/2024 merged to main)

    - Add event existence check

- Attendee Registration Check
  _Create a new branch to modify ‘collect_feedback’ function._

1. Adding Event Existence Check: Firstly, the function checks if the provided event_id exists within the events_db. If it doesn't, it prints a message stating that the event ID does not exist and returns without executing further.
2. Attendee Registration Check: Before accepting feedback, the function verifies if the attendee (identified by attendee_name) is registered for the specified event by checking their presence in the event's attendees list. If the attendee is not found, a message is printed indicating that the customer does not exist in the event's records, and the function returns without collecting feedback.
3. Feedback Collection: If the attendee is found, the function proceeds to collect their feedback. It checks if there's an existing feedback entry for the event in attendees_db; if not, it creates one. Then, it stores the attendee's feedback.

### Date and time

    - At first, just allows the user to input a number that has a pattern in the placeholder (Enter event date (YYYY-MM-DD):)

- Need date format validation
  _Date Validation:_

The try block attempts to convert the date string into a datetime object using the format "%Y-%m-%d" (which corresponds to "YYYY-MM-DD").
If this conversion fails, a ValueError is raised, and the except block is executed, printing an error message and returning False to indicate the event creation was unsuccessful due to invalid date format.

Successful Event Creation: If the date format is valid and the event ID does not already exist in the system, the event details are added to events_db, and a success message is printed.
