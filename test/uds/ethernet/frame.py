import sys

sys.path.append("../../../protocols")

from uds import *
from uds.pdu.routine_control import RoutineControl
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

service = RoutineControl()

print(service)
print(RoutineControl.SubFunction.START)