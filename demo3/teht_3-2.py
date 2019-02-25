import sys
import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../credentials.json', scope)

gc = gspread.authorize(credentials)
sht1 = gc.open("hirsimaki_raspberry-temp-hum").sheet1
sht1.append_row(["eka", "toka"])
