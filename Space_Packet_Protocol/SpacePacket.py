class SpacePacket:
    """
    A Space Packet is used to carry the data in the Space Packet Protocol.
    """
    def __init__(self,
                 packet_primary_header,
                 packet_data_field):

        self.packet_primary_header = packet_primary_header
        self.packet_data_field = packet_data_field

    def get_packet_primary_header(self):
        return self.packet_primary_header

    def get_packet_data_field(self):
        return self.packet_data_field

    def get_user_data_field(self):
        return self.packet_data_field.get_user_data_field()

    def get_bitstring(self):
        raise NotImplementedError
