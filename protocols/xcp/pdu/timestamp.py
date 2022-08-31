from ctypes import LittleEndianStructure, c_uint8, c_uint16, c_uint32, sizeof

class Timestamp(LittleEndianStructure):
    
    def __init__(self, timestamp = None, timestamp_length = 1):
        self.timestamp        = timestamp
        self.timestamp_length = timestamp_length

    def __bytes__(self):
        """
        Return bytes representation.

        Payload:
        [0:N] : Timestamp (Optional)
        """
        output = b''

        if self.timestamp and self.timestamp_length:            
            timestamp_format = c_uint8
            
            if self.timestamp_length == 1:
                timestamp_format = c_uint8
            elif self.timestamp_length == 2:
                timestamp_format = c_uint16
            elif self.timestamp_length == 4:
                timestamp_format = c_uint32
            else:
                pass # TODO : Warning
            class Payload(LittleEndianStructure):
                _pack_   = 1
                _fields_ =  [
                                ('timestamp', timestamp_format),
                            ]

            payload = Payload()
            payload.timestamp = self.timestamp

            output = bytes(payload)
        else:
            class Payload(LittleEndianStructure):
                pass

            output = bytes(Payload())

        return output