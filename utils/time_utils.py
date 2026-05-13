from datetime import datetime

def is_daytime():
    hour = datetime.now().hour
    return 6 <= hour < 18

def day_or_night():
    if is_daytime:
        return 'day'
    else:
        return 'night'