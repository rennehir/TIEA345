import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led = 21
GPIO.setup(led, GPIO.OUT)

pir = 18
GPIO.setup(pir, GPIO.IN)

while True:
  button_state = GPIO.input(button)

  if button_state == False:
    pir_state = GPIO.input(pir)
    print('Button pressed')
    print('PIR state:', pir_state)
    time.sleep(0.2)
    GPIO.output(led, 1)
  else :
    GPIO.output(led, 0)

GPIO.cleanup()
