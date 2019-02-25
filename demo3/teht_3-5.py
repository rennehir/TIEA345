import datetime
from time import sleep
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
sleep(2)
now = datetime.datetime.now()
camera.capture('/home/pi/code/TIEA345/demo3/cronimages/image' + now.isoformat() + '.jpg')
