import sys
import time
import Adafruit_DHT

while True:
  humidity, temperature = Adafruit_DHT.read_retry(11, 21)
  print 'Temperature: {0:0.1f} C    Humidity: {1:0.1f} %'.format(temperature, humidity)
  time.sleep(3)
