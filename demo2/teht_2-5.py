import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

motion_sensor = 18
GPIO.setup(motion_sensor, GPIO.IN)

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

pedestrian_signal = 22
GPIO.setup(pedestrian_signal, GPIO.OUT)

# Initial light setup for cars
GPIO.output(car_red, 0)
GPIO.output(car_yellow, 0)
GPIO.output(car_green, 1)

# Initial light setup for pedestrians
GPIO.output(pedestrian_red, 1)
GPIO.output(pedestrian_green, 0)
GPIO.output(pedestrian_signal, 0)

def set_pedestrian_signal():
  GPIO.output(pedestrian_signal, 1)

def blink_pedestrian_green():
  GPIO.output(pedestrian_green, 0)
  time.sleep(0.2)
  GPIO.output(pedestrian_green, 1)
  time.sleep(0.2)
  GPIO.output(pedestrian_green, 0)
  time.sleep(0.2)
  GPIO.output(pedestrian_green, 1)
  time.sleep(0.2)
  GPIO.output(pedestrian_green, 0)

def allow_pedestrians_crossing():
  GPIO.output(pedestrian_signal, 0)
  GPIO.output(car_green, 0)
  GPIO.output(car_yellow, 1)
  time.sleep(2)
  GPIO.output(car_yellow, 0)
  GPIO.output(car_red, 1)
  time.sleep(2)
  GPIO.output(pedestrian_red, 0)
  GPIO.output(pedestrian_green, 1)
  print('Pedestrians can cross now')

def deny_pedestrians_crossing():
  blink_pedestrian_green()
  GPIO.output(pedestrian_green, 0)
  GPIO.output(pedestrian_red, 1)
  print('Pedestrians cannot cross')
  time.sleep(2)
  GPIO.output(car_yellow, 1)
  time.sleep(1)
  GPIO.output(car_red, 0)
  GPIO.output(car_yellow, 0)
  GPIO.output(car_green, 1)
  print('Cars can go now')

def run_traffic_lights():
  allow_pedestrians_crossing()
  time.sleep(5)
  deny_pedestrians_crossing()

while True:
  button_state = GPIO.input(button)

  if button_state == False:
    set_pedestrian_signal()
    print('Pedestrian wants to cross')

    time.sleep(1.5)

    motion_sensor_state = GPIO.input(motion_sensor)

    if motion_sensor_state == 0:
      print('No cars coming, wait for green light')
      run_traffic_lights()
    else :
      print('Cars coming, please wait')
      time.sleep(5)
      run_traffic_lights()

GPIO.cleanup()
