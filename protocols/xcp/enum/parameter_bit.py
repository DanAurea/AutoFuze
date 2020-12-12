from enum import IntFlag

class RessourceBit(IntFlag):
    """
    This class describes a ressource bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    PGM                          = 0x10
    STIM                         = 0x08
    DAQ                          = 0x04
    RESERVED_1                   = 0x02
    CAL_PAG                      = 0x01
    
class CommModeBasicBit(IntFlag):
    """
    This class describes a communications mode basic bit.
    """
    OPTIONAL                     = 0x80
    SLAVE_BLOCK_MODE             = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    ADDRESS_GRANULARITY_1        = 0x04
    ADDRESS_GRANULARITY_0        = 0x02
    BYTE_ORDER                   = 0x01
    
class CommModeOptional(IntFlag):
    """
    This class describes a communications mode optional.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    INTERLEAVED_MODE             = 0x02
    MASTER_BLOCK_MODE            = 0x01
    
class CommModePgm(IntFlag):
    """
    This class describes a communications mode program.
    """
    RESERVED_7                   = 0x80
    SLAVE_BLOCK_MODE             = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    INTERLEAVED_MODE             = 0x02
    MASTER_BLOCK_MODE            = 0x01
    
class SetRequestBit(IntFlag):
    """
    This class describes a set request mode bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    CLEAR_DAQ_REQ                = 0x08
    STORE_DAQ_REQ                = 0x04
    RESERVED_2                   = 0x02
    STORE_CAL_REQ                = 0x01
    
class CurrentSessionStatusBit(IntFlag):
    """
    This class describes a current session status bit.
    """
    RESUME                       = 0x80
    DAQ_RUNNING                  = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    CLEAR_DAQ_REQ                = 0x08
    STORE_DAQ_REQ                = 0x04
    RESERVED_2                   = 0x02
    STORE_CAL_REQ                = 0x01
    
class DaqKeyBit(IntFlag):
    """
    This class describes a daq key bit.
    """
    IDENTIFICATION_FIELD_TYPE_1  = 0X80
    IDENTIFICATION_FIELD_TYPE_0  = 0X40
    ADDRESS_EXTENSION_DAQ        = 0X20
    ADDRESS_EXTENSION_ODT        = 0X10
    OPTIMISATION_TYPE_3          = 0X08
    OPTIMISATION_TYPE_2          = 0X04
    OPTIMISATION_TYPE_1          = 0X02
    OPTIMISATION_TYPE_0          = 0X01
    
class DaqPropertiesBit(IntFlag):
    """
    This class describes a daq properties bit.
    """
    OVERLOAD_EVENT               = 0x80
    OVERLOAD_MSB                 = 0x40
    PID_OFF_SUPPORTED            = 0x20
    TIMESTAMP_SUPPORTED          = 0x10
    BIT_STIM_SUPPORTED           = 0x08
    RESUME_SUPPORTED             = 0x04
    PRESCALER_SUPPORTED          = 0x02
    DAQ_CONFIG_TYPE              = 0x01
    
class SetDaqListModeBit(IntFlag):
    """
    This class describes a set daq list mode.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    PID_OFF                      = 0x20
    TIMESTAMP                    = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    DIRECTION                    = 0x02
    RESERVED_0                   = 0x01
    
class GetDaqListModeBit(IntFlag):
    """
    This class describes a get daq list mode.
    """
    RESUME                       = 0x80
    RUNNING                      = 0x40
    PID_OFF                      = 0x20
    TIMESTAMP                    = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    DIRECTION                    = 0x02
    SELECTED                     = 0x01
    
class GetDaqListInfoBit(IntFlag):
    """
    This class describes a get daq list information bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    STIM                         = 0x08
    DAQ                          = 0x04
    EVENT_FIXED                  = 0x02
    PREDEFINED                   = 0x01
    
class GetDaqEventInfoBit(IntFlag):
    """
    This class describes a get daq event information bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    STIM                         = 0x08
    DAQ                          = 0x04
    RESERVED_1                   = 0x02
    RESERVED_0                   = 0x01
    
    class TimestampModeBit(IntFlag):
    """
    This class describes a timestamp mode bit.
    """
    UNIT_3                       = 0X80
    UNIT_2                       = 0X40
    UNIT_1                       = 0X20
    UNIT_0                       = 0X10
    TIMESTAMP_FIXED              = 0X08
    SIZE_2                       = 0X04
    SIZE_1                       = 0X02
    SIZE_0                       = 0X01
    
class PagPropertiesBit(IntFlag):
    """
    This class describes a pag properties bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    RESERVED_1                   = 0x02
    FREEZE_SUPPORTED             = 0x01
    
class SetSegmentModeBit(IntFlag):
    """
    This class describes a set segment mode bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    RESERVED_1                   = 0x02
    FREEZE                       = 0x01
    
class GetSegmentModeBit(IntFlag):
    """
    This class describes a get segment mode bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    RESERVED_1                   = 0x02
    FREEZE                       = 0x01
    
class GetPageInfoBit(IntFlag):
    """
    This class describes a get page informations bit.
    """
    RESERVED_7                   = 0x80
    RESERVED_6                   = 0x40
    XCP_WRITE_ACCESS_WITH_ECU    = 0x20
    XCP_WRITE_ACCESS_WITHOUT_ECU = 0x10
    XCP_READ_ACCESS_WITH_ECU     = 0x08
    XCP_READ_ACCESS_WITHOUT_ECU  = 0x04
    ECU_ACCESS_WITH_XCP          = 0x02
    ECU_ACCESS_WITHOUT_XCP       = 0x01
    
class SetCalPageBit(IntFlag):
    """
    This class describes a set cal page bit.
    """
    ALL                          = 0x80
    RESERVED_6                   = 0x40
    RESERVED_5                   = 0x20
    RESERVED_4                   = 0x10
    RESERVED_3                   = 0x08
    RESERVED_2                   = 0x04
    XCP                          = 0x02
    ECU                          = 0x01
    
class PgmPropertiesBit(IntFlag):
    """
    This class describes a pgm properties bit.
    """
    NON_SEQ_PGM_REQUIRED         = 0X80
    NON_SEQ_PGM_SUPPORTED        = 0X40
    ENCYRPTION_REQUIRED          = 0X20
    ENCYRPTION_SUPPORTED         = 0X10
    COMPRESSION_REQUIRED         = 0X08
    COMPRESSION_SUPPORTED        = 0X04
    FUNCTIONAL_MODE              = 0X02
    ABSOLUTE_MODE                = 0X01