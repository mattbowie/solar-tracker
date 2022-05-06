import math
import datetime
import time
import RPi.GPIO as GPIO

from Sunrise_Sunset import Sunrise, Sunset
from Lat_Long_Read import lat_long
from Rise_Set_Twist import Rise_Twist, Set_Twist, T_Twist
from Motor_Control29 import Motor1, Motor2, steps2, home
from twist_tilt import Twist, Tilt
from Time import Time
from excel import excel
from openpyxl import Workbook
from ina260.controller import Controller

c = Controller(address = 0x40)

GPIO.setwarnings(False)

lat,long = lat_long() # Import Lat_Long from .txt file

N=datetime.datetime.now().timetuple().tm_yday # Counts which day of the year it is. Don't ask me how it works?!

#Return to home
home()

while True:

    #This will constantly be reading the time from the computer
    CST= datetime.datetime.now()  #Import current time and convert to decimal equivalent
    current_time_hrs = int(CST.hour)
    current_time_min = int(CST.minute)
    current_time = current_time_hrs+current_time_min/60

    #Step 1: Calculate Declination Angle
    DecAng = -math.asin(0.39779*math.cos((math.pi/180)*(0.98565*(N+10) + 1.914*math.sin((math.pi/180)*0.98565*(N-2)))))*(180/math.pi)
    
    Rise_CST = Sunrise(N, DecAng) #Sunrise Time Import
    Start = Rise_CST + 0.25  #Needs Adjust to account for GMT

    Set_CST = Sunset(N, DecAng) #Sunset Time Import
    Stop = Set_CST - 0.25  #Need it to stop early so tilt doesn't go greater than 90 degrees. Not ideal, but will hopefully get the job done. 
     
    current_twist_steps = 0
    current_tilt_steps = 0
    
    wb = Workbook()
    wb.title = "{N}"
    wb.save(f"/home/pi/Desktop/SolarTracker/Data/{N}.xlsx")
    
    
    while current_time > Start and current_time < Stop:  #Daylight operation
        
        time.sleep (1)
        current_time = Time()
        twist, Twist_steps = Twist()
        tilt, tilt_steps = Tilt()
            
        if Twist_steps < current_twist_steps:
            move_twist = abs(current_twist_steps - Twist_steps)
            Motor2(move_twist,1)
                
        elif Twist_steps > current_twist_steps:
            move_twist = abs(Twist_steps - current_twist_steps)
            Motor2(move_twist,2)
            
        if tilt_steps < current_tilt_steps:
            move_tilt = current_tilt_steps - tilt_steps
            Motor1(move_tilt,2)
                
        elif tilt_steps > current_tilt_steps:
            move_tilt = tilt_steps - current_tilt_steps
            Motor1(move_tilt,1)
            
            
        current_twist_steps = Twist_steps
        
        current_tilt_steps = tilt_steps
                    
        excel(current_time, c.voltage(), c.current(), c.power(), N)
            
        time.sleep(600)
        
    home()
    
    while current_time > Stop or current_time < Start:
        
        current_time = Time()
        time.sleep(300)
