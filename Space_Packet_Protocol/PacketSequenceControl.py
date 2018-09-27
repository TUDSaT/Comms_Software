class PacketSequenceControl:
    """
    The Packet Sequence Control contains Sequence Flags and information about the sequence count or name.
    """
    def __init__(self,
                 sequence_flags,
                 packet_sequence_count_or_packet_name):

        '''
        :param sequence_flags: 0 for a continuation segment, 1 for first segment, 2 for last segment and 3 for unsegmented user data
        :type sequence_flags: int
        :param packet_sequence_count_or_packet_name: For telemetry data sequence count, for telecommand either count or a name
        :type packet_sequence_count_or_packet_name: integer or str
        '''

        self.sequence_flags = sequence_flags
        self.packet_sequence_count_or_packet_name = packet_sequence_count_or_packet_name
