from enum import IntEnum

class MessageType(IntEnum):
    REQUEST               = 0X00 # A request expecting a response (even void)
    REQUEST_NO_RETURN     = 0X01 # A fire & forget request
    NOTIFICATION          = 0X02 # A request of a notification expecting no response
    TP_REQUEST            = 0X20 # TP request
    TP_REQUEST_NO_RETURN  = 0X21 # TP fire & forget request
    TP_NOTIFICATION       = 0X22 # TP request of a notification/event call
    TP_RESPONSE           = 0X23 # TP response
    TP_ERROR              = 0X24 # TP response containing error
    REQUEST_ACK           = 0X40 # ACK for request (optional)
    REQUEST_NO_RETURN_ACK = 0X41 # ACK for request no return (informational)
    NOTIFICATION_ACK      = 0X42 # ACK for notification (informational)
    RESPONSE              = 0X80 # The response message
    ERROR                 = 0X81 # The response containing an error
    RESPONSE_ACK          = 0XC0 # ACK for response (informational)
    ERROR_ACK             = 0XC1 # ACK for error (informational)