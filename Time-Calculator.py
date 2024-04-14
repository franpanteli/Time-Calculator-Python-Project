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
