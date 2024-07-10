def add_time(start, duration, starting_day=None):
  
    days_of_week = {
        "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
        "friday": 4, "saturday": 5, "sunday": 6
    }
    
    index_to_day = {v: k.capitalize() for k, v in days_of_week.items()}
    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    if period == 'PM':
        start_hour += 12
    
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    new_minute = total_minutes % 60
    
    total_hours = start_hour + duration_hour + extra_hour
    new_hour = total_hours % 24
    days_later = total_hours // 24
    
    new_period = 'AM' if new_hour < 12 else 'PM'
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12
    
    if starting_day:
        starting_day = starting_day.lower()
        start_day_index = days_of_week[starting_day]
        new_day_index = (start_day_index + days_later) % 7
        new_day = index_to_day[new_day_index]
    
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    
    if starting_day:
        new_time += f", {new_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
