from enum import IntEnum

class DevelopmentErrors(IntEnum):
    SOMEIPXF_E_UNINIT        = 0x01 # If any API service, GetVersionInfo is called before the transformer module was initialized
    SOMEIPXF_E_INIT_FAILED   = 0x02 # If an invalid configuration set was selected
    SOMEIPXF_E_PARAM         = 0x03 # API service called with wrong parameter
    SOMEIPXF_E_PARAM_POINTER = 0x04 # API service called with invalid pointer