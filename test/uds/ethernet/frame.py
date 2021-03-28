import sys

sys.path.append("../../../protocols")

from uds import *
from uds.pdu.ecu_reset import EcuReset
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType

service = EcuReset()

print(service)
print(bytes(service))