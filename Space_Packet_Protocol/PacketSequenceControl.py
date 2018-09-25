class PacketSequenceControl:
    """
    The Packet Sequence Control contains Sequence Flags and information about the sequence count or name.
    """
    def __init__(self,
                 sequence_flags,
                 packet_sequence_count_or_packet_name):

        self.sequence_flags = sequence_flags
        self.packet_sequence_count_or_packet_name = packet_sequence_count_or_packet_name