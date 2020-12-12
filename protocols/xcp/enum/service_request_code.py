from enum import IntEnum

class ServiceRequestCode(IntEnum):
    """
    This class describes a service request code.
    """
    SERV_RESET = 0x00
    SERV_TEXT  = 0x01