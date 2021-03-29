import enum
import sys

sys.path.append("../../../protocols")

from uds import *
from uds.pdu.session_control import SessionControl
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

service = SessionControl()

print(service)
print(bytes(service))