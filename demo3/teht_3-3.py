from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('./images/image.jpg')
camera.stop_preview()

sleep(2)

camera.resolution = (720, 540)
camera.start_preview()
sleep(2)
camera.start_recording('/home/pi/video.h264')
sleep(15)
camera.stop_recording()
camera.stop_preview()
