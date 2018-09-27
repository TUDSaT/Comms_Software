class PacketSecondaryHeader:
    """
    The Packet Secondary Header consists of either a Time Code only or an Ancillary Data Field only or both.
    """
    def __init__(self,
                 time_code_field,
                 ancillary_data_field):

        '''
        :param time_code_field: Shall consist of one of the CCSDS specified time codes
        :type time_code_field: str
        :param ancillary_data_field: Not specified by the standard, may contain additional information
        :type ancillary_data_field: str
        '''

        self.time_code_field = time_code_field
        self.ancillary_data_field = ancillary_data_field
