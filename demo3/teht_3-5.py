import datetime
from time import sleep
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
sleep(2)
now = datetime.datetime.now()
camera.capture('./cronimages/image' + now.isoformat() + '.jpg')
