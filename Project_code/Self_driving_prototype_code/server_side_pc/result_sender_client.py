# -*- coding: utf-8 -*-
"""


@author: Bhatti
"""

import socket

def send_result(result):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.10.4',5200))
    client.send(str(result).encode('utf-8'))
# =============================================================================
#     from_server = client.recv(1024)
# =============================================================================
    client.close()
# =============================================================================
#     print (from_server.decode('utf-8'))
#     if from_server.decode('utf-8') == 'OK':
#         print('chala do')
# =============================================================================
               
