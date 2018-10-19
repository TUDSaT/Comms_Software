class TransferFrame:
    """
    A Transfer Frame is used to carry the data in the Unified Space Data Link Protocol.
    """
    def __init__(self,
                 transfer_frame_primary_header,
                 transfer_frame_insert_zone,
                 transfer_frame_data_field,
                 operational_control_field,
                 frame_error_control_field):

        '''
        :param transfer_frame_primary_header: Contains information about the Frame
        :type transfer_frame_primary_header: TransferFramePrimaryHeader
        :param transfer_frame_insert_zone: Is used by the Insert Service
        :type transfer_frame_insert_zone:
        :param transfer_frame_data_field: Contains the data of the Frame
        :type transfer_frame_data_field: TransferFrameDataField
        :param operational_control_field: Provides a mechanism to report some real-time functions
        :type operational_control_field:
        :param frame_error_control_field: Provides the capability to detect errors
        :type frame_error_control_field:
        '''

        self.transfer_frame_primary_header = transfer_frame_primary_header
        self.transfer_frame_insert_zone = transfer_frame_insert_zone
        self.transfer_frame_data_field = transfer_frame_data_field
        self.operational_control_field = operational_control_field
        self.frame_error_control_field = frame_error_control_field
