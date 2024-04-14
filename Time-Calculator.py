"""
    Outline of this document:
        -> We are defining two functions, the first is called `get_days_later` and the second is called `add_time`
        -> We want to insert a time into the function, and then tell it to add another quantity of time to this 
        -> Then, to return the result of this temporal addition 
        -> With a third optional argument being given as the day of the week

    The get_days_later(days) function:
        -> We can have multiple return statements in the same Python function definition 
        -> The second function which this .py file defines has a third (optional) argument 
            -> The first function which we define here is going to be nested into the second function 
        -> The input to this first function is an integer number of days 
        -> Either one day has been entered into the function, in which case we return that it is the next day in an 
            f-string literal 
        -> Or, more than one days have been entered
        -> In which case, we are printing the number of days in an f-string literal 
        -> There is a final case, where the number of days we have left is 0 - for which we want to return a blank 
            string 
        -> This is a helper function, to be nested into and used in the second function for the project 
"""

def get_days_later(days):
    """ Format the days later into string"""
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""

"""
	The purpose of the `add_time` function:
        -> The second function we define as part of this is the `add_time(start_time, end_time, day=False)` function 
        -> This takes a time, and another amount of time to add to it, and then returns their sum 
        -> We also have a third argument which takes the day of the week, whose presence is optional 
        -> There are multiple tests for this written in the Project Task Notes.pdf file, which we want to code into this 
            function 

	Problem solving to write this function:
        -> The function has two arguments, both being times 
        -> We want to take the second argument and add it to the first, then output the results of this 
        -> So we need to first format the times (function inputs) in a way which will allow us to add them together 
            -> There are multiple different forms which these inputs can take, depending on the tests which the project
                'Task Notes.pdf' file lists 
            -> We are taking them, splitting them into hours / minutes and period (AM and PM) 
            -> Then converting them into integers, which the calculations are performed on 

	We then add the first two arguments of the function together, to calculate the total minutes and hours for the 
        sum: 
            -> Since we are working in minutes and hours, if there are an excess of minutes then we will expand this to the 
                number of hours which we have 
            -> After we have added the two times together, we need to check if the result of this exceeds midday or not 
            -> In which case, we are either operating in the PM / AM regime and this needs to be reflected in the function 
                result 
            -> After midday, we take away 12 from the result to print the number in PM format 
            -> This is to pass the function tests, in the project requirements 

	Then if the third (optional) `day` argument is inputted into the function:
		-> This means we have a time on a certain weekday, we want to add some period of time to it and return this time - 
            and the day of the week which it would land us on 
		-> This is done by storing all of the days of the week in an array, and then calculating the day which we end up on 
            by incrementing the day that the time of the first argument was given on
		-> Then including the time which we end up on as part of the return result 
		-> This is an optional argument, so the result won't include the day of the week if this third argument isn't given 

	-> Then the result of this is returned as a string 
"""

def add_time(start_time, end_time, day=False):
    
    # constants
    HOURS_IN_ONE_DAY = 24
    HOURS_IN_HALF_DAY = 12
    WEEK_DAYS = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    days_later = 0
    hours, mins = start_time.split(":")
    mins, period = mins.split(" ")
    end_time_hrs, end_time_mins = end_time.split(":")

    # Clean time data
    hours = int(hours)  # start time  hours
    mins = int(mins)  # start time  minutes
    end_time_hrs = int(end_time_hrs)  # end time hours
    end_time_mins = int(end_time_mins)  # end time minutes
    period = period.strip().lower()  # AM or PM

    # Combine start time and end time hrs and minutes
    total_mins = mins + end_time_mins
    total_hours = hours + end_time_hrs

    # Shift minutes to hour if minutes is over 60
    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if end_time_hrs or end_time_mins:
        # If `PM`, flip period to `AM` if hours over 12
        if period == "pm" and total_hours > HOURS_IN_HALF_DAY:
            # if hours over 24hr then add  days
            if total_hours % HOURS_IN_ONE_DAY >= 1.0:
                days_later += 1

        if total_hours >= HOURS_IN_HALF_DAY:
            hours_left = total_hours / HOURS_IN_ONE_DAY
            days_later += int(hours_left)

            # e.g: 54hr / 24 = 2.25 days <-- append 2 days
            # e.g.: 36hr / 24 = 1.5 days <-- append 1 days

        temp_hours = total_hours
        while True:
            # Constantly reverse period until
            # total_hours are less than half a day
            if temp_hours < HOURS_IN_HALF_DAY:
                break
            if period == "am":
                period = "pm"
            else:
                period = "am"
            temp_hours -= HOURS_IN_HALF_DAY

    """
    Recalculate Hours and Minutes 
    
     Since we have already taken care of the days,
     we now need to calculate the hours remaining.
     This can be done by subtracting the remaining days(in hours) 
     from the total hours remaining 
        
        e.g. hrs % oneday -->  55hrs % 24 = 7 ---> 7 hours remaining
    """
    remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
    remaining_mins = int(total_mins % 60)

    # Format the results
    results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
    if day:  # add the day of the week
        day = day.strip().lower()
        selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
        current_day = WEEK_DAYS[selected_day]
        results += f", {current_day.title()} {get_days_later(days_later)}"

    else:  # add the days later
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()
