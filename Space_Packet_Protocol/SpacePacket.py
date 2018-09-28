class SpacePacket:
    """
    A Space Packet is used to carry the data in the Space Packet Protocol.
    """
    def __init__(self,
                 packet_primary_header,
                 packet_data_field):

        '''
        :param packet_primary_header: Consists of the Packet Version Number, Packet Identification Field, Packet Sequence Control Field and the Packet Data Length
        :type packet_primary_header: PacketPrimaryHeader
        :param packet_data_field: Mandatory and consists of the Packet Secondary Header and the User Data Field
        :type packet_data_field: PacketDataField
        '''

        self.packet_primary_header = packet_primary_header
        self.packet_data_field = packet_data_field

    def get_bitstring(self):
        raise NotImplementedError
