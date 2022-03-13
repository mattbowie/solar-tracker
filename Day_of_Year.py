import sys
import math

def Day(month, DOM, year):

    Feb = (month+9)/12
    N2 = math.floor(Feb)

    N3 = (1+math.floor((year-4*math.floor(year/4)+2)/3))

    N1 = math.floor((275*month)/9)

    N = N1 - (N2*N3)+DOM-30
    
    return N