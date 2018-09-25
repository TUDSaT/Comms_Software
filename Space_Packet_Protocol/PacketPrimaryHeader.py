class PacketPrimaryHeader:
    """
    The Packet Primary Header contains information about the Space Packet.
    """
    def __init__(self,
                 packet_version_number,
                 packet_idenficiation,
				 packet_sequence_control,
				 packet_data_length):

        self.packet_version_number = packet_version_number
        self.packet_idenficiation = packet_idenficiation
		self.packet_sequence_control = packet_sequence_control
		self.packet_data_length = packet_data_length