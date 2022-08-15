from enum import IntEnum

# TODO: Maybe create a superclass that allow description + error code for other protocols (it would be cleaner I think)

class ErrorCode(IntEnum):
    """
    This class describes an error code.
    """
    ERR_VERIFY            = 0x32, "The slave internal program verify routine detects an error."
    ERR_GENERIC           = 0x31, "Generic error."
    ERR_MEMORY_OVERFLOW   = 0x30, "Memory overflow error."
    
    ERR_DAQ_CONFIG        = 0X2A, "DAQ configuration not valid."
    ERR_SEQUENCE          = 0X29, "Sequence error."
    ERR_SEGMENT_NOT_VALID = 0X28, "Selected segment not valid."
    ERR_MODE_NOT_VALID    = 0X27, "Selected page mode not available."
    ERR_PAGE_NOT_VALID    = 0X26, "Selected page not available."
    ERR_ACCESS_LOCKED     = 0X25, "Acess denied, Seed & Key is required."
    ERR_ACCESS_DENIED     = 0X24, "The memory location is not accessible."
    ERR_WRITE_PROTECTED   = 0X23, "The memory location is write protected."
    ERR_OUT_OF_RANGE      = 0X22, "Command syntax valid but command parameter(s) out of range."
    ERR_CMD_SYNTAX        = 0X21, "Command syntax invalid."
    ERR_CMD_UNKNOWN       = 0X20, "Unknown command or not implemented optional command."
    
    ERR_PGM_ACTIVE        = 0x12, "Command rejected because PGM is running."
    ERR_DAQ_ACTIVE        = 0x11, "Command rejected because DAQ is running."
    ERR_CMD_BUSY          = 0x10, "Command was not executed."
    
    ERR_CMD_SYNCH         = 0x00, "Command processor synchronization."

    def __new__(cls, value, description):
        obj = int.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, value, description):
        self.description = description

    def __str__(self):
        return f'{{{self._name_}, {hex(self._value_)}}} : {self.description}'