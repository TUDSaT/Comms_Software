class PacketSecondaryHeader:
    """
    The Packet Secondary Header consists of either a Time Code only or an Ancillary Data Field only or both.
    """
    def __init__(self,
                 time_code_field,
                 ancillary_data_field):

        self.time_code_field = time_code_field
        self.ancillary_data_field = ancillary_data_field