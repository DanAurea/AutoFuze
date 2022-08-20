import enum
import sys

sys.path.append("../../../protocols")

# Import enum
from uds.enum.session import Session

# Import PDU
from uds.pdu.routine_control import RoutineControl
from uds.pdu.security_access import SecurityAccess
from uds.pdu.session_control import SessionControl
from uds.pdu.tester_present import TesterPresent
from uds.pdu.transfer_data import TransferData
from uds.pdu.write_data_by_identifier import WriteDataByID

from uds.transport.ethernet.payload.diagnostic_message import DiagnosticMessage
from uds.transport.ethernet.payload.vehicle_identification import VehicleIdentificationVIN

vin_request = VehicleIdentificationVIN("0123456789ABCDEFG")
print(vin_request, bytes(vin_request))

# Craft a DoIP packet by getting Ethernet transport and craft final message as Scapy
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RoutineControl(routine_id = 0xF000)
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SecurityAccess(sub_function = SecurityAccess.SubFunction.REQUEST_SEED)
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SecurityAccess(sub_function = SecurityAccess.SubFunction.SEND_KEY, key = bytes([0x00, 0x02]))
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SessionControl(session = Session.EXTENDED_DIAGNOSTIC_SESSION)
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / TesterPresent(sub_function = TesterPresent.SubFunction.NONE)
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / TransferData(block_sequence_counter = 12, data = bytes([0x01, 0x02]))
print(ethernet_diagnostic_message)
ethernet_diagnostic_message = DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / WriteDataByID(did = 0xFD30, data = bytes([0x01, 0x02]))
print(ethernet_diagnostic_message)