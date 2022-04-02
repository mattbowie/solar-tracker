
def lat_long ():
    
    file = open('Parameters.txt')
    content = file.readlines()
    lat = float(content[3])
    long = float(content[6])
    
    return lat, long;