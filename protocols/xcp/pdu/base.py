class XCPPacketBase(object):

    def __init__(self, pid = 0x00):
        self._pid = pid
    
    def __bytes__(self):
        raise NotImplementedError()

    def is_correct_pid(self):
        return True