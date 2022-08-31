from ctypes import LittleEndianStructure, c_uint8, c_uint16

class Identification(LittleEndianStructure):
    """
    This class describes the identification field used in XCP frame.
    
    This field allow to identify nature of XCP packet sent between
    Master and Slave during XCP session.

    """
    def __init__(self, pid = None, fill = False, daq = None, daq_word = False):
        self.pid      = pid
        self.fill     = fill
        self.daq      = daq
        self.daq_word = daq_word

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:1] : PID (Optional)
        [1:2] : Fill (Optional)
        [2:3] : DAQ (Optional)
        """
        output = b''
        
        if self.pid:            
            fill_format = 0 * c_uint8
            daq_format  = 0 * c_uint8
            
            if self.fill:
                fill_format = c_uint8

            if self.daq:
                daq_format = c_uint8
            
                if self.daq_word:
                    daq_format = c_uint16

            class Payload(LittleEndianStructure):
                _pack_   = 1
                _fields_ =  [
                                ('pid', c_uint8),
                                ('fill', fill_format),
                                ('daq', daq_format),
                            ]

            payload = Payload()
            payload.pid = self.pid
            if self.daq:
                payload.daq = self.daq

            output = bytes(payload)
        else:
            class Payload(LittleEndianStructure):
                pass

            output = bytes(Payload())

        return output