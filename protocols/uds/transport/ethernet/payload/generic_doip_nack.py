from ctypes import c_uint8

from uds.transport.ethernet.message import DoIPMessage
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

class GenericDoIPNack(DoIPMessage):
    """
    Generic DoIP 
    """
    _pack_   = 1
    _fields_ =  [
                    ("nack_code", c_uint8)
                ]