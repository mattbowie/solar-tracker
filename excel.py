import openpyxl

def excel(current_time, voltage, current, power, date):
    wb = openpyxl.load_workbook(f"/media/pi/Lexar/{date}.xlsx")
    ws = wb.active
    ws.append([current_time, voltage, current, power])
    wb.save(f"/home/pi/Desktop/SolarTracker/Data/{date}.xlsx") # Put USB file path here