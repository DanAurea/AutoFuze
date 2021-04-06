from enum import IntEnum

class ReturnCode(IntEnum):
    E_OK                               = 0X00 # No error occured
    E_NOT_OK                           = 0X01 # An unspecified error occured
    SOMEIPXF_E_UNKNOWN_SERVICE         = 0X02 # The requested Service ID is unknown
    SOMEIPXF_E_UNKNOWN_METHOD          = 0X03 # The requested Method ID is unknown
    SOMEIPXF_E_NOT_READY               = 0X04 # Service ID and method ID are known. Application not running
    SOMEIPXF_E_NOT_REACHABLE           = 0X05 # System running the service is not reachable (internal code only)
    SOMEIPXF_E_TIMEOUT                 = 0X06 # A timeout occured (internal error code only)
    SOMEIPXF_E_WRONG_PROTOCOL_VERSION  = 0X07 # Version of SOME/IP not supported
    SOMEIPXF_E_WRONG_INTERFACE_VERSION = 0X08 # Interface version mismatch
    SOMEIPXF_E_MALFORMED_MESSAGE       = 0X09 # Deserialization error, so that payload cannot be deserialized
    SOMEIPXF_E_WRONG_MESSAGE_TYPE      = 0X0A # An unexpected message type was received
    # RESERVED                         = 0X0B # Reserved for generic SOME/IP errors, will be specified in future versions
    # RESERVED                         = 0X1F # Reserved for generic SOME/IP errors, will be specified in future versions
    # APPLICATION_ERRORS               = 0x20 # These errors are the application errors specified by the ClientServerInterface 
    # APPLICATION_ERRORS               = 0x5e # These errors are the application errors specified by the ClientServerInterface