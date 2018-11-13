class FARM_1:

    def __init__(self, virtual_channel_id, sliding_window_width, clcw_reporting_period):
        self.virtual_channel_id = virtual_channel_id
        self.state = 'OPEN'
        self.lockout_flag = False
        self.wait_flag = False
        self.retransmit_flag = False
        self.receiver_frame_sequence_number = 0
        self.farm_b_counter = 0
        try:
            self.sliding_window_width = int(sliding_window_width)
        except Exception as err_msg:
            print('Exception: ' + str(err_msg))
            return
        if sliding_window_width >= 2 and sliding_window_width <= 254 and (sliding_window_width % 2 == 0):
            self.sliding_window_width = sliding_window_width
        else:
            raise Exception('Invalid sliding window size')
            return
        self.positive_window_width = sliding_window_width/2
        self.negative_window_width = sliding_window_width/2
        self.clcw_reporting_period = clcw_reporting_period

    def accept(self):
        raise NotImplementedError

    def discard(self):
        raise NotImplementedError

    def report(self):
        raise NotImplementedError

    def ignore(self):
        raise NotImplementedError

    # Just for testing
    def receive_frame(self, frame):
        if frame == 'invalid_frame':                #E9
            print('Invalid frame received')
            discard()
        elif frame = 'buffer_release_signal':       #E10
            print('Buffer release signal received')
            if state == 'OPEN':
                ignore()
            elif state == 'WAIT':
                self.wait_flag = False
                self.state = 'OPEN'
            elif state == 'LOCKOUT':
                self.wait_flag = False
    
