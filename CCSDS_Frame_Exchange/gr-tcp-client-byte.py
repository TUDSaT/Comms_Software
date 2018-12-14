#!/usr/bin/env python3

import os
import socket
from pathlib import Path
from struct import unpack
from multiprocessing import Process, Queue
from packetDetector import detect

# Initialize variables
TCP_IP = '127.0.0.1'
TCP_PORT = 8002
BUFFER_SIZE = 1024
no_data_counter = 0
myFile = "test.bin"
unpackedDataStr = ''
exchangeDataStr = ''
formatStr = ''
pointer = 0
q = Queue()

# Socket initialization
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))
data = client_socket.recv(BUFFER_SIZE)
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
        exchangeDataStr += unpackedDataStr
        unpackedDataStr = ''
        try:
            if not p.is_alive():
                pointer = q.get()
                p = Process(target=detect, args=(q,pointer,exchangeDataStr,))
                p.start()
        except NameError:
            p = Process(target=detect, args=(q,pointer,exchangeDataStr,))
            p.start()
# Make sure array is completely processed
try:
    p.join()
    pointer = q.get()
    p = Process(target=detect, args=(q,pointer,exchangeDataStr,))
    p.start()
    p.join()
except NameError:
    print("Connection failed")
# Closing the socket
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()
# Save received data to file
openFile = open(myFile, "w")
openFile.write(exchangeDataStr)
openFile.close()
