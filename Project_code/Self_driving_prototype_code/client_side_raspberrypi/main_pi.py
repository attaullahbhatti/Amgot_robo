# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:26:36 2021

@author: Bhatti
"""
import time
import cv2
import arduino_controls as arduino_controls
import result_receiver_server as result_receiver_server
# import pic_client as pic_client
import camera as camera
def init():
#     frame  = camera.getImg()
#     cv2.imwrite('current.jpg',frame)
#     pic_client.send_pic()
    result = result_receiver_server.get_result()
    #print('r',result)
    #result = -7
    arduino_controls.controls(result)
while True:
    #time.sleep(0.001)
    #print(i,'callgai')
    init()




