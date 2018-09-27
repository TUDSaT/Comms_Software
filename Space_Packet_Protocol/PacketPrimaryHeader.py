class PacketPrimaryHeader:
    """
    The Packet Primary Header contains information about the Space Packet.
    """
    def __init__(self,
                 packet_version_number,
                 packet_idenficiation,
				 packet_sequence_control,
				 packet_data_length):

        '''
        :param packet_version_number: Shall be set to 0
        :type packet_version_number: int
        :param packet_idenficiation: Consists of Packet Type, Secondary Header Flag and the API
        :type packet_idenficiation: PacketIdentification
        :param packet_sequence_control: Devided into Sequence Flag and the Packet Sequence Count or Packet Name
        :type packet_sequence_control: PacketSequenceControl
        :param packet_data_length: Byte count - 1
        :type packet_data_length: int
        '''

        self.packet_version_number = packet_version_number
        self.packet_idenficiation = packet_idenficiation
        self.packet_sequence_control = packet_sequence_control
        self.packet_data_length = packet_data_length
