class SpacePacketService:
    """
    The Space Packet Service shall transfer Space Packets through the Logik Data Path.
    """
    def __init__(self,
                 space_packet,
                 apid,
                 apid_qualifier,
                 qos_requirement):

        '''
        :param space_packet: The assembled Space Packet
        :type space_packet: SpacePacket
        :param apid: Application Process Identifier
        :type apid: str
        :param apid_qualifier: Application Process Identifier Qualifier is an optional parameter to identify the naming domain of the API
        :type apid_qualifier: str
        :param qos_requirement: Quality of Service requirement
        :type qos_requirement: int
        '''

        self.space_packet = space_packet
        self.apid = apid
        self.apid_qualifier = apid_qualifier
        self.qos_requirement = qos_requirement

    def request(self):
        raise NotImplementedError

    def indication(self):
        raise NotImplementedError
