#!/usr/bin/env python3

import os
import socket
import time


# Initialize variables
TCP_IP = '127.0.0.1'
TCP_PORT = 8005
BUFFER_SIZE = 1024
msg_str = '0002AA00000000020000002A3CB87F00'
msg_bytes = bytearray.fromhex(msg_str)

# Socket initialization
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((TCP_IP, TCP_PORT))

print(msg_bytes)

while(True):
    server_socket.sendall(msg_bytes)
    time.sleep(0.1)
