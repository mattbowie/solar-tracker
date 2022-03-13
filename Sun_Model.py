import sys
import math

from Day_of_Year import Day

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

#print(f"This date is on day {N} of the year.")

#Step 1: Calculate Declination Angle
DecAng = -math.asin(0.39779*math.cos((math.pi/180)*(0.98565*(N+10) + 1.914*math.sin((math.pi/180)*0.98565*(N-2)))))*(180/math.pi)
print(f"The declination angle for the {N} day of the year is {DecAng} degrees.")

#Step 2: Hour Angle Calculation
CST = 19 # This is 7:00 pm in CST THIS IS WHERE THE TIME INPUT NEEDS TO BE
GMT = CST-6
SunLoc = -15*GMT
HrAngl = long-SunLoc
print(f"The hour angle is {HrAngl} degrees.")

#Step 3: Tilt for Panel
tilt = math.acos((math.cos(DecAng*(math.pi/180))*math.cos(HrAngl*(math.pi/180))*math.cos(lat*(math.pi/180)))+(math.sin(DecAng*(math.pi/180))*math.sin(lat*(math.pi/180))))*(180/math.pi)
print(f"The tilt angle is {tilt} degrees.") # If tilt angle is greater than 90 then it it dark outside and the panel should not be running!!!!

#Step 4: Assembly Twist
twist = math.atan(-math.tan(HrAngl*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi)

# Adjust twist to account for summer time. Twist will be greater than 90 deg at sunrise and less than -90 degrees at sunset. 
if twist > -90 and CST < 12:
    twist = twist +180
    
if twist > -90 and CST > 12:
    twist = twist -180
    
print(f"The assmembly twist is {twist} degrees.")
