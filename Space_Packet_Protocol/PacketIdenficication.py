class PacketIdentification:
    """
    The Packet Identifier contains the Packet Type and the Application Process Identifier.
    """
    def __init__(self,
                 packet_type,
                 secondary_header_flag,
				 application_process_identifier):

        'Packet Type: 0 TM - 1 TC'
        self.packet_type = packet_type
        self.secondary_header_flag = secondary_header_flag
        self.application_process_identifier = application_process_identifier
