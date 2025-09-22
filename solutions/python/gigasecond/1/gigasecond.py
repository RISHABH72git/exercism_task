from datetime import timedelta
def add(moment):
    one_gigasecond = 1_000_000_000
    return moment + timedelta(seconds=one_gigasecond)
    
