class PacketDataField:
    """
    The Packet Data Field contains the optional Packet Secondary Header and the User Data Field.
    """
    def __init__(self,
                 packet_secondary_header,
                 user_data_field):

        '''
        :param packet_secondary_header: The Secondary Header consists of either a Time Code Field only, an Ancillary Data Field only or a Time Code followed by an Ancillary Data Field
        :type packet_secondary_header: PacketSecondaryHeader
        :param user_data_field: Optional, if a Packet Secondary Header is present otherwise mandatory
        :type user_data_field: byte array
        '''

        self.packet_secondary_header = packet_secondary_header
        self.user_data_field = user_data_field
