import enum
import sys

sys.path.append("../../../protocols")

from uds import *
from uds.enum.session import Session
from uds.pdu.session_control import SessionControl
from uds.transport.ethernet.enum.payload_type import DoIPPayloadType
from uds.transport.ethernet.payload.diagnostic_message import DiagnosticMessage
from uds.transport.ethernet.payload.vehicle_identification import VehicleIdentificationVIN

diagnostic_message = DiagnosticMessage()
service            = SessionControl(session = Session.EXTENDED_DIAGNOSTIC_SESSION)

vin_request = VehicleIdentificationVIN("0123456789ABCDEFG")

print(vin_request, bytes(vin_request))

# Craft a DoIP packet by getting Ethernet transport and craft final message as Scapy
ethernet_diagnostic_message = diagnostic_message / service
print(ethernet_diagnostic_message, bytes(ethernet_diagnostic_message))