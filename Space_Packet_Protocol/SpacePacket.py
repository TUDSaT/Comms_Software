class SpacePacket:
    """
    A Space Packet is used to carry the data in the Space Packet Protocol.
    """
    def __init__(self,
                 packet_primary_header,
                 packet_data_field):

        '''
        :param packet_primary_header: Consists of the Packet Version Number, Packet Identification Field, Packet Sequence Control Field and the Packet Data Length
        :type packet_primary_header: PacketPrimaryHeader
        :param packet_data_field: Mandatory and consists of the Packet Secondary Header and the User Data Field
        :type packet_data_field: PacketDataField
        '''

        self.packet_primary_header = packet_primary_header
        self.packet_data_field = packet_data_field

    def get_binary_sequence(self):
        binary_sequence = self.append_bits(self.packet_primary_header.packet_version_number, 3) \
                        + str(self.packet_primary_header.packet_idenficiation.packet_type) \
                        + str(self.packet_primary_header.packet_idenficiation.secondary_header_flag) \
                        + self.append_bits(self.packet_primary_header.packet_idenficiation.application_process_identifier, 11) \
                        + self.append_bits(self.packet_primary_header.packet_sequence_control.sequence_flags, 2) \
                        + self.append_bits(self.packet_primary_header.packet_sequence_control.packet_sequence_count_or_packet_name, 14) \
                        + self.append_bits(self.packet_primary_header.packet_data_length, 16)
        return binary_sequence

    def append_bits(self, old_bit_array, new_length):
        new_bit_array = format(old_bit_array, '0' + str(new_length) + 'b')
        return new_bit_array
