import time
import RPi.GPIO as GPIO

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

for x in range(5):
  GPIO.output(led, GPIO.HIGH)
  time.sleep(1)

  GPIO.output(led, GPIO.LOW)
  time.sleep(1)

GPIO.cleanup()
