from PacketAssembly import PacketAssembly
class OktetStringService:
    """
    The Oktet String Service shall transfer Oktet Strings through the Logik Data Path.
    """

    'from PacketAssembly import PacketAssembly'

    def __init__(self,
                 apid,
                 apid_qualifier,
                 secondary_header_indicator,
                 qos_requirement):

        self.apid = apid
        self.apid_qualifier = apid_qualifier
        self.secondary_header_indicator = secondary_header_indicator
        self.qos_requirement = qos_requirement
        self.data_loss_indicator = False
        self.packet_assembly = {}
        self.space_packet = None

    def set_oktet_string(self, oktet_string):
        self.oktet_string = oktet_string

    def set_apid(self, apid):
        self.apid = apid

    def set_apid_qualifier(self, apid_qualifier):
        self.apid_qualifier = apid_qualifier

    def set_secondary_header_indicator(self, secondary_header_indicator):
        self.secondary_header_indicator = secondary_header_indicator

    def set_qos_requirement(self, qos_requirement):
        self.qos_requirement = qos_requirement

    def set_data_loss_indicator(self, data_loss_indicator):
        self.data_loss_indicator = data_loss_indicator

    def get_space_packet(self):
        return self.space_packet

    def request(self):
        'Adds entry to dict if not existing yet'
        'self.initial_packet_assembly = PacketAssembly(self.apid, self.apid_qualifier)'
        'self.packet_assembly[self.apid+self.apid_qualifier] = self.initial_packet_assembly'
        self.packet_assembly[self.apid+self.apid_qualifier] = PacketAssembly(self.apid, self.apid_qualifier)
        print('Successfuly assembled the packet')
        'Build the Space Packet'
        self.packet_assembly[self.apid+self.apid_qualifier].build_space_packet(self.oktet_string)
        print('Successfuly build the Space Packet')
        'Get the Space Packet'
        self.space_packet = self.packet_assembly[self.apid+self.apid_qualifier].get_space_packet()
        print('Successfuly got the Space Packet')

    def indication(self):
        raise NotImplementedError()
