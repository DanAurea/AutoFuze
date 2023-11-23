from ctypes import c_uint8, c_uint16

from protocols.some_ip_sd.pdu.option import Option

class LoadBalancingOption(Option):
    _pack_      =   1
    _fields_    =   [
                        ("reserved", c_uint8),
                        ("priority", c_uint16), # Lower value means higher priority
                        ("weight", c_uint16), # Large values means higher probability to be chosen
                    ]