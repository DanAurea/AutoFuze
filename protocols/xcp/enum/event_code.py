from enum import IntEnum

class EventCode(IntEnum):
    """
    This class describes an event code.
    """
    EV_RESUME_MODE        = 0x00
    EV_CLEAR_DAQ          = 0x01
    EV_STORE_DAQ          = 0x02
    EV_STORE_CAL          = 0x03
    EV_CMD_PENDING        = 0x05
    EV_DAQ_OVERLOAD       = 0x06
    EV_SESSION_TERMINATED = 0x07
    EV_USER               = 0xFE
    EV_TRANSPORT          = 0xFF