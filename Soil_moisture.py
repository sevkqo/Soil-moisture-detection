import nest_asyncio
nest_asyncio.apply()

TOKEN = #insert your token for Google Sheets here

import time
import serial
import gspread

sa = gspread.service_account(filename=r#insert path to JSON file here)
sh = sa.open("Arduino_wilgotnosc")

wks = sh.worksheet("Arkusz1")
wks1 = sh.worksheet("Wykres procentowy")

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)

i = 1 
f = 60 #period of getting new data from sensors [min]

while (True):
    rawdata = []
    rawdata.append(str(arduino.readline()))
    from_arduino = ''.join(rawdata)
    print(from_arduino)
    
    result = [0,0,0]
    j1 = 0
    j2 = 0
    j3 = 0
    
    #algorithm to organize incoming data from arduino (in case of getting 4-digits input from sensors)
    if (from_arduino[5].isdigit() == True):
        j1 = 1
        if (from_arduino[11].isdigit() == True):
            j2 = 1
            if (from_arduino[17].isdigit() == True):  
                j3 = 1
        elif (from_arduino[16].isdigit() == True):
            j3 = 1
    elif(from_arduino[10].isdigit() == True):
        j2 = 1
        if (from_arduino[16].isdigit() == True):      
            j3 = 1
    elif (from_arduino[16].isdigit() == True):
        j3 = 1
                
    result[0] = int(from_arduino[2:5+j1])
    result[1] = int(from_arduino[7+j1:10+j1+j2])
    result[2] = int(from_arduino[12+j1+j2:15+j1+j2+j3])
    
    #saving data from sensors to first worksheet
    wks.update_cell(i+1, 1, i)
    wks.update_cell(i+1, 2, result[0])
    wks.update_cell(i+1, 3, result[1])
    wks.update_cell(i+1, 4, result[2])
    
    #counting data from sensors to the soil moisture in percent
    result[0] = result[0]/10
    result[1] = result[1]/10
    result[2] = result[2]/10
    
    #saving data from sensors to second worksheet
    wks1.update_cell(i+1, 1, i)
    wks1.update_cell(i+1, 2, result[0])
    wks1.update_cell(i+1, 3, result[1])
    wks1.update_cell(i+1, 4, result[2])
    
    #data to Discord bot
    wks1.update_cell(2, 7, result[0])
    wks1.update_cell(2, 8, result[1])
    wks1.update_cell(2, 9, result[2])  
    
    time.sleep(f*60)
    i += 1