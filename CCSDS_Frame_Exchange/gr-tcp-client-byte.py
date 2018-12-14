#!/usr/bin/env python3

import os
import socket
from pathlib import Path
from struct import unpack
from multiprocessing import Process, Queue
from packetDetector import detect
import time

# Initialize variables
TCP_IP = '127.0.0.1'
TCP_PORT = 8001
BUFFER_SIZE = 1024
no_data_counter = 0
myFile = "test.bin"
unpackedDataStr = ''
formatStr = ''
pointer = 0
q = Queue()

# Socket initialization
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))
data = client_socket.recv(BUFFER_SIZE)

# Check if output file already exists and open it
if not os.path.exists(myFile):
    openFile = open(myFile, "w")
    openFile.close()
#openFile = open(myFile, "r+")

# Receive data
while no_data_counter < 10:
    openFile = open(myFile, "a+")
    data = client_socket.recv(BUFFER_SIZE)
    if data == b'':
        no_data_counter += 1
    else:
        no_data_counter = 0
        formatStr = ''.join(["c" for i in range(str(data).count("\\"))])
        unpackedDataList = unpack(formatStr, data)
        unpackedDataStr = ''.join([str(unpackedDataList[x])[-2:-1] for x, val in enumerate(unpackedDataList)])
        openFile.write(unpackedDataStr)
        unpackedDataStr = ''
        openFile.close()
        try:
            if not p.is_alive():
                pointer = q.get()
                p = Process(target=detect, args=(q,pointer,))
                p.start()
        except NameError:
            p = Process(target=detect, args=(q,pointer,))
            p.start()

# Make sure file is fully processed
try:
    p.join()
    pointer = q.get()
    p = Process(target=detect, args=(q,pointer,))
    p.start()
    p.join()
except NameError:
    print("Connection failed")

# Closing the socket
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()
