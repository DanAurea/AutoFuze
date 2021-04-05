from enum import IntEnum

class ServiceID(IntEnum):
    """
    This class enumerates all service id hex code for UDS.
    """
    DIAGNOSTIC_SESSION_CONTROL         = 0X10
    ECU_RESET                          = 0X11
    CLEAR_DIAGNOSTIC_INFORMATION       = 0X14
    READ_DTC_INFORMATION               = 0X19
    READ_DATA_BY_IDENTIFIER            = 0X22
    READ_MEMORY_BY_ADDRESS             = 0X23
    READ_SCALING_DATA_BY_IDENTIFIER    = 0X24
    SECURITY_ACCESS                    = 0X27
    COMMUNICATION_CONTROL              = 0X28
    AUTHENTICATION                     = 0X29
    READ_DATA_BY_IDENTIFIER_PERIODIC   = 0X2A
    DYNAMICALLY_DEFINE_DATA_IDENTIFIER = 0X2C
    WRITE_DATA_BY_IDENTIFIER           = 0X2E
    INPUT_OUTPUT_CONTROL_BY_IDENTIFIER = 0X2F
    ROUTINE_CONTROL                    = 0X31
    REQUEST_DOWNLOAD                   = 0X34
    REQUEST_UPLOAD                     = 0X35
    TRANSFER_DATA                      = 0X36
    REQUEST_TRANSFER_EXIT              = 0X37
    REQUEST_FILE_TRANSFER              = 0X38
    WRITE_MEMORY_BY_ADDRESS            = 0X3D
    TESTER_PRESENT                     = 0X3E
    NEGATIVE_RESPONSE                  = 0X7F
    ACCESS_TIMING_PARAMETERS           = 0X83
    SECURED_DATA_TRANSMISSION          = 0X84
    CONTROL_DTC_SETTINGS               = 0X85
    RESPONSE_ON_EVENT                  = 0X86
    LINK_CONTROL                       = 0XC7