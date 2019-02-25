import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../credentials.json', scope)

gc = gspread.authorize(credentials)

sht1 = gc.open("hirsimaki_raspberry-temp-hum").sheet1

while True:
  humidity, temperature = Adafruit_DHT.read_retry(11, 21)
  print 'Temperature: {0:0.1f} C    Humidity: {1:0.1f} %'.format(temperature, humidity)
  sht1.append_row([humidity, temperature])
  time.sleep(3)
