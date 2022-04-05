import math
import datetime
from Lat_Long_Read import lat_long


lat,long = lat_long() 

def Twist():
    while True:
        
        CST= datetime.datetime.now()  #Import current time and convert to decimal equivalent
        current_time_hrs = int(CST.hour)
        current_time_min = int(CST.minute)
        current_time = current_time_hrs+current_time_min/60
        SunLoc = -15*(current_time-12)
        HrAngl = long-SunLoc
    
        twist = math.atan(-math.tan(HrAngl*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi)

        # Adjust twist to account for summer time. Twist will be greater than 90 deg at sunrise and less than -90 degrees at sunset. 
        if twist < 0 and current_time < 18:
            twist = twist +180
    
        if twist > 0 and current_time > 18:   #ISSUEEEEEEE
            twist = twist -180
        
        Twist_steps = twist/0.067
    
        return Twist_steps
    
def Tilt():
    while True:
        
        N=datetime.datetime.now().timetuple().tm_yday
        
        CST= datetime.datetime.now()  #Import current time and convert to decimal equivalent
        current_time_hrs = int(CST.hour)
        current_time_min = int(CST.minute)
        current_time = current_time_hrs+current_time_min/60
        SunLoc = -15*(current_time-12)
        HrAngl = long-SunLoc
        
        DecAng = -math.asin(0.39779*math.cos((math.pi/180)*(0.98565*(N+10) + 1.914*math.sin((math.pi/180)*0.98565*(N-2)))))*(180/math.pi)
        
        tilt = math.acos((math.cos(DecAng*(math.pi/180))*math.cos(HrAngl*(math.pi/180))*math.cos(lat*(math.pi/180)))+(math.sin(DecAng*(math.pi/180))*math.sin(lat*(math.pi/180))))*(180/math.pi)
        #print(f"The tilt before angle is {tilt} degrees.") 
        tilt = 90-tilt
        tilt_steps = tilt /0.067
        
        return tilt_steps
    