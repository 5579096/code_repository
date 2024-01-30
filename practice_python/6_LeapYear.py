"""
Leap Year Checker Function

Objective:
Write a function named 'is_leap_year' to determine whether a given year is a leap year.

Function Parameter:
year (integer): The year to be checked.

Instructions:
- The function should return 'True' if the 'year' is a leap year and 'False' otherwise.
- A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
- Use conditional statements to implement the leap year check.

Example Test Cases:
1. is_leap_year(2020) should return 'True'.
2. is_leap_year(1900) should return 'False'.
3. is_leap_year(2000) should return 'True'.
4. is_leap_year(2019) should return 'False'.
"""


def is_leap_year(year):
    if year % 100 == 0: #find which input year are century year first
        if year % 400 != 0: #condition check year leap Year for century year
            return False
        else:
            return True
    
    elif year % 4 == 0: #condition check year leap Year for non-century year
        return True
    
    else:
        return False

""" by chat gpt

def is_leap_year(year):
    # Leap year is divisible by 4
    if year % 4 == 0:
        # But, end-of-century years must be divisible by 400
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
"""



# Test cases
print(is_leap_year(2020))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(2019))  # Expected output: False
