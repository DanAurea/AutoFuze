from enum import IntEnum

class OBDMode(IntEnum):
    SHOW_CURRENT_DATA           = 0x01
    SHOW_FREEZE_FRAME_DATA      = 0x02
    SHOW_STORED_DTC             = 0x03
    CLEAR_DTC                   = 0x04
    TEST_RESULT_OXYGEN_SENSOR   = 0x05
    TEST_RESULT_SYSTEM          = 0x06
    SHOW_PENDING_DTC            = 0x07
    CONTROL_OPERATION           = 0x08
    REQUEST_VEHICLE_INFORMATION = 0x09
    REQUEST_PERMANENT_DTC       = 0x0A