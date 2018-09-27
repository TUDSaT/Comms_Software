import datetime
from PacketIdenficication import PacketIdentification
from PacketSequenceControl import PacketSequenceControl
from PacketPrimaryHeader import PacketPrimaryHeader
from PacketSecondaryHeader import PacketSecondaryHeader
from PacketDataField import PacketDataField
from SpacePacket import SpacePacket

class PacketAssembly:

    def __init__(self,
                 apid,
                 apid_qualifier):

         '''
         :param apid: Application Process Identifier
         :type apid: str
         :param apid_qualifier: Application Process Identifier Qualifier is an optional parameter to identify the naming domain of the API
         :type apid_qualifier: str
         '''

         self.adip = apid
         self.apid_qualifier = apid_qualifier
         self.packet_sequence_count = 0
         self.space_packet = None
         self.packet_version_number = 0

    def get_apid(self):
        return self.apid

    def get_apid_qualifier(self):
        return self.apid_qualifier

    def get_packet_sequence_count(self):
        return self.packet_sequence_count

    def get_space_packet(self):
        return self.space_packet

    def build_space_packet(self, octet_string):
        self.packet_idenficiation = PacketIdentification(0, 1, self.adip)
        self.packet_sequence_control = PacketSequenceControl(0, self.packet_sequence_count)
        self.packet_data_length = len(octet_string) - 1
        self.packet_primary_header = PacketPrimaryHeader(self.packet_version_number,
                                                         self.packet_idenficiation,
                                                         self.packet_sequence_control,
                                                         self.packet_data_length)
        'ToDo: This timestamp is not as recommended in the standard - work to do!'
        self.time_code_field = datetime.datetime.utcnow()
        'No Ancillary Data Field, could be used for applied coding identification'
        self.packet_secondary_header = PacketSecondaryHeader(self.time_code_field,
                                                             None)
        self.user_data_field = octet_string
        self.packet_data_field = PacketDataField(self.packet_secondary_header,
                                                 octet_string)
        self.space_packet = SpacePacket(self.packet_primary_header, self.packet_data_field)
