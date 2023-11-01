from datetime import timedelta, date
import calendar

def get_birthdays_per_week(users: list) -> dict:
    _today_ = date.today()
    
    weekdays = {day: [] for day in calendar.day_name} 
    
    for user in users: 
        bd_this_year = user['birthday'].replace(year=_today_.year) 
        
        bd_next_year = user['birthday'].replace(year=_today_.year + 1) 
        
        upcoming_birthdays = [] 
        
        if _today_ <= bd_this_year <= _today_ + timedelta(days=6):
            upcoming_birthdays.append(bd_this_year)
            
        if _today_ <= bd_next_year <= _today_ + timedelta(days=6):
            upcoming_birthdays.append(bd_next_year)
        
        for upcoming_birthday in upcoming_birthdays:
            weekday = calendar.day_name[upcoming_birthday.weekday()] 
            if weekday in ['Saturday', 'Sunday']: 
                weekday = 'Monday'
            weekdays[weekday].append(user['name']) 
    
    weekdays = {a: b for a, b in weekdays.items() if b} 
    
    return weekdays