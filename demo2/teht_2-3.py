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

while True:
  button_state = GPIO.input(button)

  if button_state = True:
    GPIO.output(car_red, 1)
    GPIO.output(car_yellow, 1)
    GPIO.output(car_green, 1)

GPIO.cleanup()
