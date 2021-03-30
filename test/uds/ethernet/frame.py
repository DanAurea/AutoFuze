import enum
import sys

sys.path.append("../../../protocols")

from uds import *
from uds.pdu.session_control import SessionControl
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.payload.diagnostic_message import DiagnosticMessage

diagnostic_message = DiagnosticMessage()
service            = SessionControl()

print(service)

# Craft a DoIP packet by getting Ethernet transport and craft final message as Scapy
ethernet_diagnostic_message = diagnostic_message / service
print(ethernet_diagnostic_message)