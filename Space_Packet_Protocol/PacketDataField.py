class PacketDataField:
    """
    The Packet Data Field contains the optional Packet Secondary Header and the User Data Field.
    """
    def __init__(self,
                 packet_secondary_header,
                 user_data_field):

        self.packet_secondary_header = packet_secondary_header
        self.user_data_field = user_data_field