# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:43:04 2021

@author: Bhatti
"""

import socket

def get_result():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # so that server does not close very quickly
    server.bind(('192.168.10.7',5200))
    server.listen(1)
    #print('listening...')
    conn, addr = server.accept()
    from_client = ''
    data = conn.recv(1024)
    from_client += str(data.decode('utf-8'))
    print (from_client)
    #conn.send("OK".encode('utf-8'))
    conn.close()
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    #print ("closed")
    return int(from_client)
#get_result()

