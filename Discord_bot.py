import nest_asyncio
nest_asyncio.apply()

from discord.ext import tasks, commands
import gspread
import datetime

sa = gspread.service_account(filename=r#insert path to JSON file here)
sh = sa.open("Arduino_wilgotnosc")

wks = sh.worksheet("Arkusz1")
wks1 = sh.worksheet("Wykres procentowy")

result = [0,0,0]

TOKEN = #insert your token for Google Sheets here

bot = commands.Bot(command_prefix="!")

#limit of soil moisture to send notifications
soil_moisture_1 = 50
soil_moisture_2 = 50
soil_moisture_3 = 50

#part of day when bot can send notifications
tod_start = datetime.time(16)
tod_end = datetime.time(22)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')  
    message.start()

@tasks.loop(minutes = 60)
async def message():
    tod = datetime.datetime.now().time()
    if (tod_start <= tod <= tod_end):
        channel = bot.get_channel(#insert ID of Discord channel here (data type: Int)) #connect with channel on discord
        result[0] = wks1.cell(col = 7, row = 2).value #download data from Google Sheets
        result[1] = wks1.cell(col = 8, row = 2).value #download data from Google Sheets
        result[2] = wks1.cell(col = 9, row = 2).value #download data from Google Sheets
        for i in range (len(result)):
            k = result[i]
            for j in range (len(k)):
                if (k[j] == ','):
                    k = k[:j] + '.' + k[j+1:] #swap , to . for correct read data
                    result[i] = k
                    result[i] = float(result[i])
    
        if (result[0] < soil_moisture_1):
            await channel.send('Water the plant no. 1!')
        if (result[1] < soil_moisture_2):
            await channel.send('Water the plant no. 2!')
        if (result[2] < soil_moisture_3):
            await channel.send('Water the plant no. 3!')      

bot.run(TOKEN)

