class SpacePacketService:
    """
    The Space Packet Service shall transfer Space Packets through the Logik Data Path.
    """
    def __init__(self,
                 space_packet,
                 apid,
                 apid_qualifier,
                 qos_requirement):

        self.space_packet = space_packet
        self.apid = apid
        self.apid_qualifier = apid_qualifier
        self.qos_requirement = qos_requirement

    def set_space_packet(self, space_packet):
        self.space_packet = space_packet

    def set_apid(self, apid):
        self.apid = apid

    def set_apid_qualifier(self, apid_qualifier):
        self.apid_qualifier = apid_qualifier

    def set_qos_requirement(self, qos_requirement):
        self.qos_requirement = qos_requirement

    def request(self):

    def indication(self):
