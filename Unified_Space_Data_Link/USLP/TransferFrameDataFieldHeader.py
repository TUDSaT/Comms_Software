class TransferFrameDataFieldHeader:
    '''
    The Transfer Frame Data Field Header contains information about the Transfer Frame Data Field
    '''
    def __init__(self,
                 TFDZ_construction_rules,
                 USLP_protocol_identifier,
                 first_header_last_valid_octet_pointer):

        '''
        :param TFDZ_construction_rules: Shoud be used to identify how the protocol organizes the user data.
        :type TFDZ_construction_rules:
        :param USLP_protocol_identifier: Identifies the protocol, procedure, or type of data in the Transfer Frame Data Zone
        :type USLP_protocol_identifier:
        :param first_header_last_valid_octet_pointer: Contains an offset of te Transfer Frame Data Zone, dependng on the value of USLP_protocol_identifier.
        :type first_header_last_valid_octet_pointer:
        '''

        self.TFDZ_construction_rules = TFDZ_construction_rules
        self.USLP_protocol_identifier = USLP_protocol_identifier
        self.first_header_last_valid_octet_pointer = first_header_last_valid_octet_pointer
