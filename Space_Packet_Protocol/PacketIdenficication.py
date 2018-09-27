class PacketIdentification:
    """
    The Packet Identifier contains the Packet Type and the Application Process Identifier.
    """
    def __init__(self,
                 packet_type,
                 secondary_header_flag,
				 application_process_identifier):

        '''
        :param packet_type: Used to distinguish if the packet contains telemetry (0) or telecommand (1) data
        :type packet_type: int
        :param secondary_header_flag: Indicates if a Secondary Header is present or not
        :type secondary_header_flag: bool
        :param application_process_identifier: Unique only in its naming domain
        :type application_process_identifier: str
        '''

        'Packet Type: 0 TM - 1 TC'
        self.packet_type = packet_type
        self.secondary_header_flag = secondary_header_flag
        self.application_process_identifier = application_process_identifier
