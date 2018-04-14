"""
@author: Ivo Weihert
@date: 14.04.2018
@organisation: TU Darmstadt Space Technology e.V.

Test script receiving accelometer data via can bus on pyboard
Note: run receiver first!
can class documentation: https://docs.micropython.org/en/latest/pyboard/library/pyb.CAN.html
"""
from pyb import CAN
can = CAN(1, CAN.NORMAL)								#select can 1 (Y3,Y4) in normal mode
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))	#(bank, mode, fifo, params, *, rtr) - important: fifo & ID's
while (True):
	if can.any(0)==True:								#check the fifo for incomming data
		Data=can.recv(0)								#reveive the data from the fifo; Data[0:ID , 1:RTR, 2:FMIval, 3:Payload]
		if Data[0]==123:								#the Axis information is put in the can ID: 123=X, 124=Y, 125=Z
			Axis='X-Axis'
		if Data[0]==124:
			Axis='Y-Axis'
		if Data[0]==125:
			Axis='Z-Axis'
		Value=Data[3]									#getting the Value from the Data tuple
		print (Axis, Value)								#output
		pyb.LED(2).toggle()								#green LED for received data visualization
		pyb.delay(10)
	if can.any(0)==False:								#as long there is no data on the bus, flash red LED for visualization
		pyb.LED(1).toggle()
		pyb.delay(100)