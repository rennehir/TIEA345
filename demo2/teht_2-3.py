import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

car_red = 16
GPIO.setup(car_red, GPIO.OUT)

car_yellow = 20
GPIO.setup(car_yellow, GPIO.OUT)

car_green = 21
GPIO.setup(car_green, GPIO.OUT)

pedestrian_red = 23
GPIO.setup(pedestrian_red, GPIO.OUT)

pedestrian_green = 24
GPIO.setup(pedestrian_green, GPIO.OUT)

# Initial light setup
GPIO.output(car_red, 0)
GPIO.output(car_yellow, 0)
GPIO.output(car_green, 1)
GPIO.output(pedestrian_red, 1)
GPIO.output(pedestrian_green, 0)

def allow_pedestrians_crossing():
  print('Pedestrians')

while True:
  button_state = GPIO.input(button)

  if button_state == False:
    time.sleep(0.2)
    allow_pedestrians_crossing()
    time.sleep(0.2)

GPIO.cleanup()
