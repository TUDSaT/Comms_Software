from PacketAssembly import PacketAssembly
class OktetStringService:
    """
    The Oktet String Service shall transfer Oktet Strings through the Logik Data Path.
    """

    def __init__(self,
                 apid,
                 apid_qualifier,
                 secondary_header_indicator,
                 qos_requirement):

        '''
        :param apid: Application Process Identifier
        :type apid: str
        :param apid_qualifier: Application Process Identifier Qualifier is an optional parameter to identify the naming domain of the API
        :type apid_qualifier: str
        :param secondary_header_indicator: Indicates if a secondary header is present
        :type secondary_header_indicator: bool
        :param qos_requirement: Quality of Service requirement
        :type qos_requirement: int
        '''
        self.apid = apid
        self.apid_qualifier = apid_qualifier
        self.secondary_header_indicator = secondary_header_indicator
        self.qos_requirement = qos_requirement
        self.data_loss_indicator = False
        self.packet_assembly = {}
        self.space_packet = None

    def request(self):
        'Adds entry to dict if not existing yet'
        self.packet_assembly[self.apid+self.apid_qualifier] = PacketAssembly(self.apid, self.apid_qualifier)
        print('Successfuly assembled the packet')
        'Build the Space Packet'
        self.packet_assembly[self.apid+self.apid_qualifier].build_space_packet(self.oktet_string)
        print('Successfuly build the Space Packet')
        'Get the Space Packet'
        self.space_packet = self.packet_assembly[self.apid+self.apid_qualifier].space_packet
        print('Successfuly got the Space Packet')

    def indication(self):
        raise NotImplementedError()
