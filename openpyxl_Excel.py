import openpyxl
from openpyxl import load_workbook

def excel (date, current_time, voltage, current):
    
    #wb = Workbook() # Creates new workbook
    #ws.title = date # Add to main loop possibly when Rise is equal to start??
    
    #import date and current time code here
    
    wb = load_workbook(f'{date}.xlsx')
    ws = wb.active
    
    ws.append([date, current_time, voltage, current])
    
    wb.save(f'/media/pi/USB20FD/{date}.xlsx') # Put USB file path here


