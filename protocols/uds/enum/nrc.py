from enum import IntEnum

class NRC(IntEnum):
    """
    This class enumerates all Negative Response Code.
    """
    GENERAL_REJECT                               = 0X10
    SERVICE_NOT_SUPPORTED                        = 0X11
    SUB_FUNCTION_NOT_SUPPORTED                   = 0X12
    INCORRECT_MESSAGE_LENGTH_OR_INVALID_FORMAT   = 0X13
    RESPONSE_TOO_LONG                            = 0X14
    BUSY_REPEAT_REQUEST                          = 0X21
    CONDITIONS_NOT_CORRECT                       = 0X22
    REQUEST_SEQUENCE_ERROR                       = 0X24
    NO_RESPONSE_FROM_SUBNET_COMPONENT            = 0X25
    FAILURE_PREVENT_EXECUTION_OF_REQUEST_ACTION  = 0X26
    REQUEST_OUT_OF_RANGE                         = 0X31
    SECURITY_ACCESS_DENIED                       = 0X33
    INVALID_KEY                                  = 0X35
    EXCEED_NUMBER_OF_ATTEMPTS                    = 0X36
    REQUEST_TIME_DELAY_NOT_EXPIRED               = 0X37
    UPLOAD_DOWNLOAD_NOT_ACCEPTED                 = 0X70
    TRANSFER_DATA_SUSPENDED                      = 0X71
    GENERAL_PROGRAMMING_FAILURE                  = 0X72
    WRONG_BLOCK_SEQUENCE_COUNTER                 = 0X73
    REQUEST_CORRECTLY_RECEIVED_RESPONSE_PENDING  = 0X78
    SUB_FUNCTION_NOT_SUPPORTED_IN_ACTIVE_SESSION = 0X7E
    SERVICE_NOT_SUPPORTED_IN_ACTIVE_SESSION      = 0X7F