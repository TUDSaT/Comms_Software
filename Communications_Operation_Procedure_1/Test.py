from FARM_1 import FARM_1


try:
    farm = FARM_1(0, 2, 2)
except Exception as err_msg:
    print( 'Exception: ' + str(err_msg))

farm.receive_frame('invalid_frame')
