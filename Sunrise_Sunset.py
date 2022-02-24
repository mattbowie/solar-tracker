import sys
import math
import datetime

initFile=open(r"Parameters.txt","r")
fields=initFile.readlines()
initFile.close()

latitude=float(fields[3])
longitude=float(fields[6])

N = datetime.datetime.now().timetuple().tm_yday

print(N)

decl = -23.45*math.cos((math.pi/180)*(360/365)*(N+10))

HA1 = (math.cos((math.pi/180)*90.833))/(math.cos((math.pi/180)*latitude)*math.cos((math.pi/180)*decl))

HA2 = math.tan((math.pi/180)*latitude)*math.tan((math.pi/180)*decl)

HA3 = math.acos(HA1-HA2)*(180/math.pi)

B = 360*((N-81)/365)

EQT = 9.87*math.sin(2*B*(math.pi/180))-7.53*math.cos((math.pi/180)*B)-1.5*math.sin((math.pi/180)*B)

Sunrise_Min_UTC = 720-4*(longitude+HA3)-EQT
Sunrise_Hrs_UTC = Sunrise_Min_UTC/60
#Rise_CST = Sunrise_Hrs_UTC-6

hours = int(Sunrise_Hrs_UTC)
minutes = (Sunrise_Hrs_UTC*60)%60
seconds = (Sunrise_Hrs_UTC*3600)%60

Sunset_Min_UTC = 720-4*(longitude-HA3)-EQT
Sunset_Hrs_UTC = Sunset_Min_UTC/60
#Set_CST = Sunset_Hrs_UTC-6

hours2 = int(Sunset_Hrs_UTC)
minutes2 = (Sunset_Hrs_UTC*60)%60
seconds2 = (Sunset_Hrs_UTC*3600)%60

print("Sunrise: %d:%02d.%02d"%(hours,minutes,seconds))
print("Sunset: %d:%02d.%02d"%(hours2,minutes2,seconds2))