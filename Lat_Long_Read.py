
def lat_long ():
    
    file = open('/home/pi/Desktop/SolarTracker/solar-tracker/Parameters.txt')
    content = file.readlines()
    lat = float(content[3])
    long = float(content[6])
    
    return lat, long;