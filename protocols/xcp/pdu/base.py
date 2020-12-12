class Base(object):

    def __init__(self, pid = 0x00):
        self.pid = pid

    def is_correct_pid(self):
        return True