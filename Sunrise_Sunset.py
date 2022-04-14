import math
from Lat_Long_Read import lat_long

lat,long = lat_long()

def Sunrise (N2,decl):
    
    HA1 = (math.cos((math.pi/180)*90.833))/(math.cos((math.pi/180)*lat)*math.cos((math.pi/180)*decl))
    HA2 = math.tan((math.pi/180)*lat)*math.tan((math.pi/180)*decl)
    HA3 = math.acos(HA1-HA2)*(180/math.pi)

    B = 360*((N2-81)/365)

    EQT = 9.87*math.sin(2*B*(math.pi/180))-7.53*math.cos((math.pi/180)*B)-1.5*math.sin((math.pi/180)*B)

    Sunrise_Min_UTC = 720-4*(long+HA3)-EQT
    Sunrise_Hrs_UTC = Sunrise_Min_UTC/60
    Rise_CST = Sunrise_Hrs_UTC-6
    
    return Rise_CST

def Sunset (N2, decl):
    HA1 = (math.cos((math.pi/180)*90.833))/(math.cos((math.pi/180)*lat)*math.cos((math.pi/180)*decl))
    HA2 = math.tan((math.pi/180)*lat)*math.tan((math.pi/180)*decl)
    HA3 = math.acos(HA1-HA2)*(180/math.pi)

    B = 360*((N2-81)/365)

    EQT = 9.87*math.sin(2*B*(math.pi/180))-7.53*math.cos((math.pi/180)*B)-1.5*math.sin((math.pi/180)*B)

    Sunset_Min_UTC = 720-4*(long-HA3)-EQT
    Sunset_Hrs_UTC = Sunset_Min_UTC/60
    Set_CST = Sunset_Hrs_UTC-6
    
    return Set_CST


