class TransferFrameDataField:
    '''
    The Transfer Frame Data Field contains the data that should be delivered by the frame.
    '''
    def __init__(self,
                 transfer_frame_data_field_header,
                 transfer_frame_data_zone):

        '''
        :param transfer_frame_data_field_header: Contains information about the Transfer Frame Data Field
        :type transfer_frame_data_field_header: TransferFrameDataFieldHeader
        :param transfer_frame_data_zone: Contains the real data
        :type transfer_frame_data_zone: str
        '''

        self.transfer_frame_data_field_header = transfer_frame_data_field_header
        self.transfer_frame_data_zone = transfer_frame_data_zone
