import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led = 21
GPIO.setup(led, GPIO.OUT)

while True:
  input_state = GPIO.input(button)
  if input_state == False:
    print('Button pressed')
    time.sleep(0.2)
    GPIO.output(led, 1)
  else :
    GPIO.output(led, 0)

GPIO.cleanup()
