import sys
import time
import socket
import time
import traceback
import cv2
from imutils.video import VideoStream
import imagezmq
import RPi.GPIO as GPIO

sender = imagezmq.ImageSender(connect_to='tcp://192.168.10.9:5555')

rpi_name = socket.gethostname()  # send RPi hostname with each image
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)  # allow camera sensor to warm up
jpeg_quality = 95  # 0 to 100, higher is better quality, 95 is cv2 default
try:
    while True:  # send images as stream until Ctrl-C
        image = picam.read()
        time.sleep(0.15)
        ret_code, jpg_buffer = cv2.imencode(
            ".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
        reply_from_mac = sender.send_jpg(rpi_name, jpg_buffer)
        # above line shows how to capture REP reply text from Mac
except (KeyboardInterrupt, SystemExit):
    print('ctrl C is pressed')
    picam.stop()  # stop the camera thread
    sender.close()  # close the ZMQ socket and context
    sys.exit()