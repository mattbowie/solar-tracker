import openpyxl
from openpyxl import load_workbook

def excel (date, current_time, voltage, current):
    
   #import date and current time code here
    
    wb = load_workbook(f'{date}.xlsx')
    ws = wb.active
    
    ws.append([date, current_time, voltage, current])
    
    wb.save(f'/media/pi/USB20FD/{date}.xlsx') # Put USB file path here
