class TruncatedTransferFramePrimaryHeader:

    def __init__(self,
                 transfer_frame_version_number,
                 spacecraft_ID,
                 source_or_destination_ID,
                 virtual_channel_ID,
                 multiplexer_access_point_ID,
                 end_of_frame_primary_header_flag):

        self.transfer_frame_version_number = transfer_frame_version_number
        self.spacecraft_ID = spacecraft_ID
        self.source_or_destination_ID = source_or_destination_ID
        self.virtual_channel_ID = virtual_channel_ID
        self.multiplexer_access_point_ID = multiplexer_access_point_ID
        self.end_of_frame_primary_header_flag = end_of_frame_primary_header_flag
