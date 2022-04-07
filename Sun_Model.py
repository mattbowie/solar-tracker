import math
import datetime
import time
import RPi.GPIO as GPIO

from Sunrise_Sunset import Sunrise, Sunset
from Lat_Long_Read import lat_long
from Rise_Set_Twist import Rise_Twist, Set_Twist, T_Twist
from Motor_Control29 import Motor1, Motor2, steps2, home
from twist_tilt import Twist, Tilt
GPIO.setwarnings(False)

lat,long = lat_long() # Import Lat_Long from .txt file

N=datetime.datetime.now().timetuple().tm_yday # Counts which day of the year it is. Don't ask me how it works?!

print ('System is homing')
home()

while True:

    #This will constantly be reading the time from the computer
    CST= datetime.datetime.now()  #Import current time and convert to decimal equivalent
    current_time_hrs = int(CST.hour)
    current_time_min = int(CST.minute)
    current_time = current_time_hrs+current_time_min/60
    #print(current_time)

    #Step 1: Calculate Declination Angle
    DecAng = -math.asin(0.39779*math.cos((math.pi/180)*(0.98565*(N+10) + 1.914*math.sin((math.pi/180)*0.98565*(N-2)))))*(180/math.pi)

    #Step 2: Hour Angle Calculation
    #GMT = current_time-6
    SunLoc = -15*(current_time-12)
    HrAngl = long-SunLoc

    #Step 3: Tilt for Panel
    tilt = math.acos((math.cos(DecAng*(math.pi/180))*math.cos(HrAngl*(math.pi/180))*math.cos(lat*(math.pi/180)))+(math.sin(DecAng*(math.pi/180))*math.sin(lat*(math.pi/180))))*(180/math.pi)
    #print(f"The tilt before angle is {tilt} degrees.") 
    tilt = 90-tilt
    #print(f"The tilt after angle is {tilt} degrees.") # If tilt angle is greater than 90 then it it dark outside and the panel should not be running!!!!

    #Step 4: Assembly Twist
    twist = math.atan(-math.tan(HrAngl*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi)
    #print(f'Twist = {twist}')

    # Adjust twist to account for summer time. Twist will be greater than 90 deg at sunrise and less than -90 degrees at sunset. 
    #if twist < 0 and current_time < 16:
        #twist = twist +180
    
    #if twist > 0 and current_time > 20:   #ISSUEEEEEEE
        #twist = twist -180
    
    Rise_CST = Sunrise(N, DecAng) #Sunrise Time Import
    Start = Rise_CST - 0.25  # Start at 15 minutes before Sunrise

    Set_CST = Sunset(N, DecAng) #Sunset Time Import
    Stop = Set_CST + 0.25   # Stop at 15 minutes after Sunset
    
    
    #Twist_steps = twist/0.067    #Calculates the number of steps it needs to turn from zero
    #tilt_steps = tilt /0.067
    
    current_twist_steps = 0
    current_tilt_steps = 0
    
    
    while current_time > Start and current_time < Stop:  #Daylight operation
        
        time.sleep (1)
        Twist_steps = Twist()
        tilt_steps = Tilt()
    
        print(f'Twist steps at Current Time = {Twist_steps}')
        
        print(f'Tilt steps at Current Time = {tilt_steps}')
        
        
        if Twist_steps < current_twist_steps:
            move_twist = abs(current_twist_steps - Twist_steps)
            print(f'Twist Steps Moved 1 = {move_twist}')
            Motor2(move_twist,1)   #Should move motor in opposite direction from sunrise move_twist amount of steps
                
        elif Twist_steps > current_twist_steps:
            move_twist = abs(Twist_steps - current_twist_steps)
            print(f'Twist Steps Moved 2 = {move_twist}')
            Motor2(move_twist,2)
            
        if tilt_steps < current_tilt_steps:
            move_tilt = current_tilt_steps - tilt_steps
            print(f'Tilt Steps Moved 1 = {move_tilt}')
            Motor1(move_tilt,2)
                
        elif tilt_steps > current_tilt_steps:
            move_tilt = tilt_steps - current_tilt_steps
            print(f'Tilt Steps Moved 2 = {move_tilt}')
            Motor1(move_tilt,1)
            
        if current_twist_steps == 0 and Twist_steps > 0:
            current_twist_steps = current_twist_steps + move_twist
            
        elif current_twist_steps ==0 and Twist_steps < 0:
            current_twist_steps = current_twist_steps - move_twist
        
        else:
            current_twist_steps = current_twist_steps - move_twist
        
        if move_tilt > current_tilt_steps:
            current_tilt_steps = current_tilt_steps + move_tilt
        
        elif move_tilt < current_tilt_steps:
            current_tilt_steps = current_tilt_steps - move_tilt
            
        print(f'current twist steps = {current_twist_steps}')
        
        print(f'current tilt steps = {current_tilt_steps}')
        
        print(' ')
            
        time.sleep(300)
        






