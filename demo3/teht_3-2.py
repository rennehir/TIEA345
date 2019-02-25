import sys
import time
import datetime
import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../credentials.json', scope)
gc = gspread.authorize(credentials)
sht1 = gc.open("hirsimaki_raspberry-temp-hum").sheet1

sensor = Adafruit_DHT.DHT11
pin = 21

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

  if humidity is not None and temperature is not None:
    now = datetime.datetime.now()
    sht1.append_row([now.isoformat(), temperature, humidity])
  else:
    print("Failed to get reading. Try again!")

  time.sleep(5)
