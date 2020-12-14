from struct import pack

class Identification(object):
    """
    This class describes the identification field used in XCP frame.
    
    This field allow to identify nature of XCP packet sent between
    Master and Slave during XCP session.

    """
    def __init__(self, pid = 0xFE, fill = 0x00, daq = None):
        self._pid  = pid
        self._fill = fill
        self._daq  = daq

    def __bytes__(self):
        identification_bytes = bytearray()

        identification_bytes.extend(pack("<B", self._pid))

        if self._fill:
            identification_bytes.extend(pack("<B", self._fill))

        if self._daq:
            identification_bytes.extend(pack("<B", self._daq))

        return bytes(identification_bytes)