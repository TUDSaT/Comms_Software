class SpacePacket:
    """
    A Space Packet is used to carry the data in the Space Packet Protocol.
    """
    def __init__(self,
                 packet_primary_header,
                 packet_data_field):

        self.packet_primary_header = packet_primary_header
        self.packet_data_field = packet_data_field