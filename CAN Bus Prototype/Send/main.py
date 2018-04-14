"""
@author: Ivo Weihert
@date: 14.04.2018
@organisation: TU Darmstadt Space Technology e.V.

Test script transmitting data from the accelometer via can bus on pyboard
Note: run receiver first!
can class documentation: https://docs.micropython.org/en/latest/pyboard/library/pyb.CAN.html
Accel class documentation: http://docs.micropython.org/en/v1.9.3/pyboard/library/pyb.Accel.html
"""
from pyb import CAN
accel = pyb.Accel()										
can = CAN(1, CAN.NORMAL)								#select can 1 (Y3,Y4) in normal mode
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))	#(bank, mode, fifo, params, *, rtr) - important: fifo & ID's
while (True):
	Data_X=str(accel.x())								#get the x value from the accelerometer
	can.send(Data_X,123)								#send x-value via can bus, Axis Information is put in can ID 123=X, 124=Y, 125=Z
	pyb.delay(500)										#delay for better visualization
	Data_Y=str(accel.y())
	can.send(Data_Y,124)
	pyb.delay(500)
	Data_Z=str(accel.z())
	can.send(Data_Z,125)
	pyb.delay(500)