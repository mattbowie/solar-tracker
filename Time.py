import datetime

def Time ():
    CST= datetime.datetime.now()  #Import current time and convert to decimal equivalent
    current_time_hrs = int(CST.hour)
    current_time_min = int(CST.minute)
    current_time = current_time_hrs+current_time_min/60
    
    return current_time