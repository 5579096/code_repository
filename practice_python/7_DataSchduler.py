"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

import datetime



def date_passed(todays_date, scheduled_date):
    word_list_today = []
    word_list_sch = []
    x = datetime.datetime.now()

    month_names = ["January",   "February", "March",    "April",
               "May",       "June",     "July",     "August",
               "September", "October",  "November", "December"]

    months = {name : (index + 1) for index, name in enumerate(month_names)}

    for word in todays_date.split():
        word_list_today.append(word)
        word_only = ""
        for char in word_list_today[0]:
            if char.isnumeric():
                word_only += char
            word_list_today[0] = word_only
    word_list_today.append(x.strftime("%Y"))
    #print(word_list_today)

    for word in scheduled_date.split():
        word_list_sch.append(word)
        word_only = "" 
        for char in word_list_sch[0]:
            if char.isnumeric():
                word_only += char
            word_list_sch[0] = word_only
    word_list_sch.append(x.strftime("%Y"))
    #print(word_list_sch)
    
    
    td_date = int(word_list_today[0])
    td_month = int(months.get(word_list_today[1]))
    td_year = int(word_list_today[2])

    sh_date = int(word_list_sch[0])
    sh_month = int(months.get(word_list_sch[1]))
    sh_year = int(word_list_sch[2])

   
    td_day = datetime.datetime(td_year,td_month,td_date)
    sh_day = datetime.datetime(sh_year,sh_month,sh_date)
    
    if td_day > sh_day:
        return print("Scheduled date has passed")
    elif td_day < sh_day:
        return print("Scheduled date is yet to pass")
    else:
        return print("Scheduled date is today")

   

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
