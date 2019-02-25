import datetime
from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO

camera = PiCamera()

motion_sensor = 18
GPIO.setup(motion_sensor, GPIO.IN)

while True:
    motion_sensor_state = GPIO.input(motion_sensor)

    if motion_sensor_state == 1:
        camera.start_preview()
        sleep(2)
        now = datetime.datetime.now()
        camera.capture('./images/image' + now.isoformat() + '.jpg')
        sleep(10)
