import enum
import socket
import sys

sys.path.append("../../protocols")

# Import enum
from uds.enum.nrc import NRC
from uds.enum.session import Session
from uds.enum.service_id import ServiceID

# Import PDU
from uds.pdu.access_timing_parameters import AccessTimingParameters
from uds.pdu.clear_diagnostic_information import ClearDiagnosticInformation
from uds.pdu.communication_control import CommunicationControl
from uds.pdu.control_dtc_settings import ControlDTCSettings
from uds.pdu.ecu_reset import EcuReset
from uds.pdu.input_output_control_by_identifier import IOControlByID
from uds.pdu.link_control import LinkControl
from uds.pdu.negative_response import NegativeResponse
from uds.pdu.read_data_by_identifier import ReadDataByID
from uds.pdu.read_data_by_identifier_periodic import ReadDataByIDPeriodic
from uds.pdu.read_memory_by_address import ReadMemoryByAddress
from uds.pdu.read_scaling_data_by_identifier import ReadScalingDataByID
from uds.pdu.request_download import RequestDownload
from uds.pdu.request_file_transfer import RequestFileTransfer
from uds.pdu.request_upload import RequestUpload
from uds.pdu.request_transfer_exit import RequestTransferExit
from uds.pdu.response_on_event import ResponseOnEvent
from uds.pdu.routine_control import RoutineControl
from uds.pdu.security_access import SecurityAccess
from uds.pdu.session_control import SessionControl
from uds.pdu.tester_present import TesterPresent
from uds.pdu.transfer_data import TransferData
from uds.pdu.write_data_by_identifier import WriteDataByID

from uds.transport.ethernet.payload import diagnostic_message as eth

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 13400)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    message_list = [ 
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / AccessTimingParameters(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / AccessTimingParameters(sub_function = AccessTimingParameters.SubFunction.SET_TIMING_PARAMETERS_TO_GIVEN_VALUES, timing_param_record = bytes([0x01, 0x02])),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ClearDiagnosticInformation(dtc_group = 0xFFFFFF),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / CommunicationControl(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / CommunicationControl(sub_function = CommunicationControl.SubFunction.ENHANCED_ADDRESS_INFORMATION, node_id = 0x1234),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ControlDTCSettings(settings = [0x800000, 0x402012]),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / EcuReset(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / IOControlByID(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / IOControlByID(did = 0xFF12, parameter = IOControlByID.Parameter.SHORT_TERM_ADJUSTEMENT, option_record = bytes([0x01, 0xFF])),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / LinkControl(sub_function = LinkControl.SubFunction.VERIFY_TRANSITION_FIXED_PARAMETER, link_control_id = 0x00F0),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / LinkControl(sub_function = LinkControl.SubFunction.VERIFY_TRANSITION_SPECIFIC_PARAMATER, link_record = 0x00F0F1),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / LinkControl(sub_function = LinkControl.SubFunction.TRANSITION_MODE),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / NegativeResponse(request_service_id = ServiceID.ECU_RESET, nrc = NRC.GENERAL_REJECT),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ReadDataByID(did = 0xF010),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ReadDataByIDPeriodic(did_list = [0xF010, 0xF020]),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ReadMemoryByAddress(parameters_length = 0x00),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ReadMemoryByAddress(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ReadScalingDataByID(did = 0xF012),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RequestDownload(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RequestFileTransfer(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RequestFileTransfer(mode = RequestFileTransfer.Mode.DELETE_FILE, file_path_name_length = len('test.txt'), file_path_name = 'test.txt'),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RequestTransferExit(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RequestUpload(),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / ResponseOnEvent(sub_function = ResponseOnEvent.SubFunction.STORE_EVENT),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / RoutineControl(routine_id = 0xF000),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SecurityAccess(sub_function = SecurityAccess.SubFunction.REQUEST_SEED),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SecurityAccess(sub_function = SecurityAccess.SubFunction.SEND_KEY, key = bytes([0x00, 0x02])),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / SessionControl(session = Session.EXTENDED_DIAGNOSTIC_SESSION),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / TesterPresent(sub_function = TesterPresent.SubFunction.NONE),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / TransferData(block_sequence_counter = 12, data = bytes([0x01, 0x02])),
                    eth.DiagnosticMessage(source_address = 0x1020, target_address = 0xEE00) / WriteDataByID(did = 0xFD30, data = bytes([0x01, 0x02])),
                ]
    
    # Send crafted DoIP packets
    for message in message_list:
        sock.send(bytes(message))
    
finally:
    print('closing socket')
    sock.close()