import enum
import socket
import sys
import time
sys.path.append("../../protocols")

# Import enum
from uds.enum import *

# Import PDU
from uds.pdu import *
from uds.transport.ethernet.payload import diagnostic_message as eth

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 13400)
print('connecting to %s port %s' % server_address)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(server_address)
sock.settimeout(2)

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
        print(bytes(message))
        sock.send(bytes(message))
finally:
    print('closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()