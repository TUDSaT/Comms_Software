'This example should test and explain the usage of the Space Packet Protocol'

import urllib.request
from OktetStringService import OktetStringService
from SpacePacket import SpacePacket

'Number of the used spacecraft transponder'
apid = 4
'Spacecraft number in SATNOGS DB'
apid_qualifier =  40379
'The secondary header is used to indicate the addition of a Timestamp to the Space Packet'
secondary_header_indicator = True
'Quality of service - not implemented'
qos_requirement = 0

'Download example data'
'ToDo: Correctly convert oktet_string to binary'
oktet_string = urllib.request.urlopen("https://network.satnogs.org/media/data_obs/260763/data_260763_2018-09-26T10-34-05").read()

'Create Oktet String Service instance'
oktet_string_service = OktetStringService(apid,
                                          apid_qualifier,
                                          secondary_header_indicator,
                                          qos_requirement)

'Input example data'
oktet_string_service.oktet_string = oktet_string

'Request to send it'
oktet_string_service.request()

'Get the Packet'
space_packet = oktet_string_service.space_packet

'Output User Data Field'
print(space_packet.packet_data_field.user_data_field)

'Print binary sequence'
print("Packet primary header representation in bits: " + space_packet.get_binary_sequence())

print("Packet length in bit: " + str(len(space_packet.get_binary_sequence())))
