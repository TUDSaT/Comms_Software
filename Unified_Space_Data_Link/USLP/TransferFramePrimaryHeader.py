class TransferPrimaryHeader:
    '''
    The Transfer Frame Primary Header contains information about Transfer Frame
    '''
    def __init__(self,
                 transfer_frame_version_number,
                 spacecraft_ID,
                 source_or_destination_ID,
                 virtual_channel_ID,
                 multiplexer_access_point_ID,
                 end_of_frame_primary_header_flag,
                 frame_length,
                 bypass_sequence_control_flag,
                 command_control_flag,
                 spare,
                 operational_control_field_flag,
                 virtual_channel_sequence_counter_length,
                 virtual_channel_sequence_counter_value):

        '''
        :param transfer_frame_version_number: Transfer Frame Version Number
        :type transfer_frame_version_number: str
        :param spacecraft_ID: Spacecraft ID
        :type spacecraft_ID: str
        :param source_or_destination_ID:
        :param virtual_channel_ID:
        :param multiplexer_access_point_ID:
        :param end_of_frame_primary_header_flag:
        :param frame_length:
        :param bypass_sequence_control_flag:
        :param command_control_flag:
        :param spare:
        :param operational_control_field_flag:
        :param virtual_channel_sequence_counter_length:
        :param virtual_channel_sequence_counter_value:
        '''

        self.transfer_frame_version_number = transfer_frame_version_number
        self.spacecraft_ID = spacecraft_ID
        self.source_or_destination_ID = source_or_destination_ID
        self.virtual_channel_ID = virtual_channel_ID
        self.multiplexer_access_point_ID = multiplexer_access_point_ID
        self.end_of_frame_primary_header_flag = end_of_frame_primary_header_flag
        self.frame_length = frame_length
        self.bypass_sequence_control_flag = bypass_sequence_control_flag
        self.command_control_flag = command_control_flag
        self.spare = spare
        self.operational_control_field_flag = operational_control_field_flag
        self.virtual_channel_sequence_counter_length = virtual_channel_sequence_counter_length
        self.virtual_channel_sequence_counter_value = virtual_channel_sequence_counter_value

    def getMCID(self):
        '''
        docstring test

        :param test: tesparameter
        :type test: int
        :returns: Returns the Master Channel ID.
        '''
        return str(self.transfer_frame_version_number)\
               + str(self.spacecraft_ID)

    def getGVCID(self):
        return str(self.transfer_frame_version_number)\
               + str(self.spacecraft_ID)\
               + str(self.virtual_channel_ID)

    def getGMAPID(self):
        return str(self.transfer_frame_version_number)\
               + str(self.spacecraft_ID)\
               + str(self.virtual_channel_ID)\
               + str(self.multiplexer_access_point_ID)
