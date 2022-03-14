import math
import datetime

initFile=open(r"Parameters.txt","r")
fields=initFile.readlines()
initFile.close()

lat=float(fields[3])
long=float(fields[6])

N=datetime.datetime.now().timetuple().tm_yday

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
