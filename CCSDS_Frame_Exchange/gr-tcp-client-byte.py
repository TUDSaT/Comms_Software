#!/usr/bin/env python3

import os
import socket
from pathlib import Path
from struct import unpack

# Initialize variables
TCP_IP = '127.0.0.1'
TCP_PORT = 8001
BUFFER_SIZE = 1024
no_data_counter = 0
myFile = "test.bin"
unpackedDataStr = ''
formatStr = ''

# Socket initialization
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))
data = client_socket.recv(BUFFER_SIZE)

# Check if output file already exists and open it
if not os.path.exists(myFile):
    openFile = open(myFile, "w")
    openFile.close()
openFile = open(myFile, "r+")

# Receive data
while no_data_counter < 10:
    data = client_socket.recv(BUFFER_SIZE)
    if data == b'':
        no_data_counter += 1
    else:
        no_data_counter = 0
    formatStr = ''.join(["c" for i in range(str(data).count("\\"))])
    unpackedDataList = unpack(formatStr, data)
    unpackedDataStr = ''.join([str(unpackedDataList[x])[-2:-1] for x, val in enumerate(unpackedDataList)])
    print("Received " + str(len(unpackedDataList)) + " byte:", unpackedDataStr)
    openFile.write(unpackedDataStr)
    unpackedDataStr = ''

# Closing the socket
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()
openFile.close()
