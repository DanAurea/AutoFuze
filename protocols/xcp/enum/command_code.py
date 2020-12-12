from enum import IntEnum

class StandardCommandCode(IntEnum):
    """
    This class describes a standard command code.
    """
    CONNECT                 = 0xFF
    DISCONNECT              = 0xFE
    GET_STATUS              = 0xFD
    SYNCH                   = 0xFC
    
    GET_COMM_MODE_INFO      = 0xFB
    GET_ID                  = 0xFA
    SET_REQUEST             = 0xF9
    GET_SEED                = 0xF8
    UNLOCK                  = 0xF7
    SET_MTA                 = 0xF6
    UPLOAD                  = 0xF5
    SHORT_UPLOAD            = 0xF4
    BUILD_CHECKSUM          = 0xF3
    
    TRANSPORT_LAYER_CMD     = 0XF2
    USER_CMD                = 0XF1
    
class CalibrationCommand(IntEnum):
    """
    This class describes a calibration command.
    """
    DOWNLOAD                = 0xF0
    DOWNLOAD_NEXT           = 0xEF
    DOWNLOAD_MAX            = 0xEE
    SHORT_DOWNLOAD          = 0xED
    MODIFY_BITS             = 0xEC
    
class PageSwitchingCommand(IntEnum):
    """
    This class describes a page switching command.
    """
    SET_CAL_PAGE            = 0xEB
    GET_CAL_PAGE            = 0xEA
    
    GET_PAG_PROCESSOR_INFO  = 0xE9
    GET_SEGMENT_INFO        = 0xE8
    GET_PAGE_INFO           = 0xE7
    SET_SEGMENT_MODE        = 0xE6
    GET_SEGMENT_MODE        = 0xE5
    COPY_CAL_PAGE           = 0xE4
    
class DataAcquisitionCommand(IntEnum):
    """
    This class describes a data acquisition command.
    """
    CLEAR_DAQ_LIST          = 0XE3
    SET_DAQ_PTR             = 0XE2
    WRITE_DAQ               = 0XE1
    SET_DAQ_LIST_MODE       = 0XE0
    GET_DAQ_LIST_MODE       = 0XDF
    START_STOP_DAQ_LIST     = 0XDE
    START_STOP_SYNCH        = 0XDD
    
    GET_DAQ_CLOCK           = 0XDC
    READ_DAQ                = 0XDB
    GET_DAQ_PROCESSOR_INFO  = 0XDA
    GET_DAQ_RESOLUTION_INFO = 0XD9
    GET_DAQ_LIST_INFO       = 0XD8
    GET_DAQ_EVENT_INFO      = 0XD7
    
    FREE_DAQ                = 0XD6
    ALLOC_DAQ               = 0XD5
    ALLOC_ODT               = 0XD4
    ALLOC_ODT_ENTRY         = 0XD3
    
class NvmProgrammingCommand(IntEnum):
    """
    This class describes a nvm programming command.
    """
    PROGRAM_START           = 0XD2
    PROGRAM_CLEAR           = 0XD1
    PROGRAM                 = 0XD0
    PROGRAM_RESET           = 0XCF
    
    GET_PGM_PROCESSOR_INFO  = 0XCE
    GET_SECTOR_INFO         = 0XCD
    PROGRAM_PREPARE         = 0XCC
    PROGRAM_FORMAT          = 0XCB
    PROGRAM_NEXT            = 0XCA
    PROGRAM_MAX             = 0XC9
    PROGRAM_VERIFY          = 0XC8
    
class ReservedCommand(IntEnum):
    """
    This class describes a reserved command (not defined in Vector's documentation).
    """
    RESERVED_8              = 0xC7
    RESERVED_7              = 0xC6
    RESERVED_6              = 0xC5
    RESERVED_5              = 0xC4
    RESERVED_4              = 0xC3
    RESERVED_3              = 0xC2
    RESERVED_2              = 0xC1
    RESERVED_1              = 0xC0

class CommandCode(object):
    """
    This class describes a command code.
    """

    def __init__(self, code = 0xC0):
        self._code = code

    def type(self):
        """
        Return type of command corresponding to command enum for more convenient reading.
        """
        if self._code in range(StandardCommandCode.USER_CMD, StandardCommandCode.CONNECT + 1):
            return StandardCommandCode(self._code)
        elif self._code in range(CalibrationCommand.MODIFY_BITS, CalibrationCommand.DOWNLOAD + 1):
            return CalibrationCommand(self._code)
        elif self._code in range(PageSwitchingCommand.COPY_CAL_PAGE, PageSwitchingCommand.SET_CAL_PAGE + 1):
            return PageSwitchingCommand(self._code)
        elif self._code in range(DataAcquisitionCommand.ALLOC_ODT_ENTRY, DataAcquisitionCommand.CLEAR_DAQ_LIST + 1):
            return DataAcquisitionCommand(self._code)
        elif self._code in range(NvmProgrammingCommand.PROGRAM_VERIFY, NvmProgrammingCommand.PROGRAM_START + 1):
            return NvmProgrammingCommand(self._code)
        elif self._code in range(ReservedCommand.RESERVED_1, ReservedCommand.RESERVED_8 + 1):
            return ReservedCommand(self._code)
        else:
            return None


if __name__ == "__main__":
    c = CommandCode()
    print(c.type())