from enum import IntEnum

class AddressExtension(IntEnum):
    """
    This class describes an address extension.
    """
    ADDRESS_EXTENSION_FREE = 0x00
    ADDRESS_EXTENSION_ODT  = 0x01
    ADDRESS_EXTENSION_DAQ  = 0x03