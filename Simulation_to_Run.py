import math
import datetime
import time
import RPi.GPIO as GPIO

from Day_of_Year import Day
from Motor_Control_Sim import Motor1, Motor2, steps2, home
from Time import Time
GPIO.setwarnings(False)

lat = 37.211749
long = -93.291829

#Determine Day of Year
month = input('What month of the year are you in? Enter a numeric value between 1 and 12.\n')
month = int(month)

DOM = input('What day of the month is it? Enter a numeric value bewtween 1 and 31.\n')
DOM = int(DOM)

year = input('What year is it? Example 2022. \n')
year = int(year)

N = Day(month, DOM, year)

time = [5.75, 6.0, 6.25, 6.5, 6.75, 7, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16, 16.25, 16.5, 16.75, 17, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5]  #Running simulation from 11 am to 3 pm

current_twist_steps = 0
current_tilt_steps = 0

#Return to home
home()

for x in time:
    
    #Step 1: Calculate Declination Angle
    DecAng = -math.asin(0.39779*math.cos((math.pi/180)*(0.98565*(N+10) + 1.914*math.sin((math.pi/180)*0.98565*(N-2)))))*(180/math.pi)

    #Step 2: Hour Angle Calculation
    CST = x
    GMT = CST-6
    SunLoc = -15*GMT
    HrAngl = long-SunLoc

    #Step 3: Tilt for Panel
    tilt_reg = math.acos((math.cos(DecAng*(math.pi/180))*math.cos(HrAngl*(math.pi/180))*math.cos(lat*(math.pi/180)))+(math.sin(DecAng*(math.pi/180))*math.sin(lat*(math.pi/180))))*(180/math.pi)
    tilt_adj = 90-tilt_reg
    
    #Step 4: Assembly Twist
    twist = math.atan(-math.tan(HrAngl*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi)

    # Adjust twist to account for summer time. Twist will be greater than 90 deg at sunrise and less than -90 degrees at sunset. 
    if twist < 0 and CST < 10:
        twist = twist +180
    
    if twist > 0 and CST > 14:
        twist = twist -180
        
    Twist_steps = twist/.067
    tilt_steps = tilt_adj/.067
    
    
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
                
home()