"""
@author: Bhatti

"""

import sys
import img_preprocessing as img_preprocessing
import result_sender_client as result_sender_client
def init():
    result = img_preprocessing.image_preprocessing()
# =============================================================================
#     For debugging
#     print('image is preprocessed')
# =============================================================================
    result_sender_client.send_result(-round((result)/2))
try:    
    while True:
        init()
except (KeyboardInterrupt, SystemExit):
    print('ctrl C is pressed')
    sys.exit() 
    
