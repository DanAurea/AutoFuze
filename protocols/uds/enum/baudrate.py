import enum

class BaudRate(enum.IntEnum):
    """
    Define baud rate that can be used in UDS standard.
    """
    BAUD_9600    = 0x01
    BAUD_19200   = 0x02
    BAUD_38400   = 0x03
    BAUD_57600   = 0x04
    BAUD_115200  = 0x05
    BAUD_125000  = 0x10
    BAUD_250000  = 0x11
    BAUD_500000  = 0x12
    BAUD_1000000 = 0x13