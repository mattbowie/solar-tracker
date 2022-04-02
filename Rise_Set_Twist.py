import math

from Lat_Long_Read import lat_long
lat,long = lat_long()

def Rise_Twist(Rise_CST):
    #GMT1 = Rise_CST-6
    Rise_Loc = -15*Rise_CST
    HrAngl_Rise = long-Rise_Loc
    R_Twist = float(math.atan(-math.tan(HrAngl_Rise*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi))
    
    if R_Twist > -90 and Rise_CST < 18:
        R_Twist = R_Twist +180
    
    if R_Twist > -90 and Rise_CST > 18:
        R_twist = R_twist -180
    
    return R_Twist

def Set_Twist(Set_CST):
    #GMT2 = Set_CST-6
    Set_Loc = -15*Set_CST
    HrAngl_Set = long-Set_Loc
    S_Twist = math.atan(-math.tan(HrAngl_Set*(math.pi/180))/math.sin(lat*(math.pi/180)))*(180/math.pi) 
    
    if S_Twist > -90 and Set_CST < 18:
        S_Twist = S_Twist +180
    
    if S_Twist > -90 and Set_CST > 18:
        S_Twist = S_Twist -180
    
    return S_Twist

def T_Twist(Rise_Twist, Set_Twist):
    Total_Twist = Rise_Twist-Set_Twist
    
    return Total_Twist


    
    
    