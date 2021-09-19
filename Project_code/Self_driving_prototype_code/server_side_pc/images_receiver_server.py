import sys
import numpy as np
import cv2
import imagezmq

# instantiate image_hub
image_hub = imagezmq.ImageHub()

image_count = 0
first_image = True

try:
    while True:  # receive images until Ctrl-C is pressed
        sent_from, jpg_buffer = image_hub.recv_jpg()
        image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)
        cv2.imwrite('current.jpeg',image)
# =============================================================================
#         cv2.imshow('current.jpeg',image)
#         cv2.waitKey(1)
# =============================================================================
        image_hub.send_reply(b'OK')  # REP reply
        
except (KeyboardInterrupt, SystemExit):
    print('ctrl C is pressed')
    image_hub.close()
    sys.exit()
    