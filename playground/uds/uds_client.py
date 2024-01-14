import enum
import socket
import sys
import time
sys.path.append("../../protocols")

# Import enum
from uds.enum import *

# Import PDU
from uds.pdu import *
from uds.transport.ethernet.payload.diagnostic_message import DiagnosticMessage as uds_doip

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 13400)
print('connecting to %s port %s' % server_address)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(server_address)
sock.settimeout(2)

try:
    doip_layer = uds_doip(source_address = 0x1020, target_address = 0xEE00)
    message_list = [ 
                        AccessTimingParameters(),
                        AccessTimingParameters(sub_function = AccessTimingParameters.SubFunction.SET_TIMING_PARAMETERS_TO_GIVEN_VALUES, timing_param_record = bytes([0x01, 0x02])),
                        ClearDiagnosticInformation(dtc_group = 0xFFFFFF),
                        CommunicationControl(),
                        CommunicationControl(sub_function = CommunicationControl.SubFunction.ENHANCED_ADDRESS_INFORMATION, node_id = 0x1234),
                        ControlDTCSettings(settings = [0x800000, 0x402012]),
                        EcuReset(),
                        IOControlByID(),
                        IOControlByID(did = 0xFF12, parameter = IOControlByID.Parameter.SHORT_TERM_ADJUSTEMENT, option_record = bytes([0x01, 0xFF])),
                        LinkControl(sub_function = LinkControl.SubFunction.VERIFY_TRANSITION_FIXED_PARAMETER, link_control_id = 0x00F0),
                        LinkControl(sub_function = LinkControl.SubFunction.VERIFY_TRANSITION_SPECIFIC_PARAMATER, link_record = 0x00F0F1),
                        LinkControl(sub_function = LinkControl.SubFunction.TRANSITION_MODE),
                        NegativeResponse(request_service_id = ServiceID.ECU_RESET, nrc = NRC.GENERAL_REJECT),
                        ReadDataByID(did = 0xF010),
                        ReadDataByIDPeriodic(did_list = [0xF010, 0xF020]),
                        ReadMemoryByAddress(parameters_length = 0x00),
                        ReadMemoryByAddress(),
                        ReadScalingDataByID(did = 0xF012),
                        RequestDownload(),
                        RequestFileTransfer(),
                        RequestFileTransfer(mode = RequestFileTransfer.Mode.DELETE_FILE, file_path_name_length = len('test.txt'), file_path_name = 'test.txt'),
                        RequestTransferExit(),
                        RequestUpload(),
                        ResponseOnEvent(sub_function = ResponseOnEvent.SubFunction.STORE_EVENT),
                        RoutineControl(routine_id = 0xF000),
                        SecurityAccess(sub_function = SecurityAccess.SubFunction.REQUEST_SEED),
                        SecurityAccess(sub_function = SecurityAccess.SubFunction.SEND_KEY, key = bytes([0x00, 0x02])),
                        SessionControl(session = Session.EXTENDED_DIAGNOSTIC_SESSION),
                        TesterPresent(sub_function = TesterPresent.SubFunction.NONE),
                        TransferData(block_sequence_counter = 12, data = bytes([0x01, 0x02])),
                        WriteDataByID(did = 0xFD30, data = bytes([0x01, 0x02])),
                    ]
    
    # Send crafted DoIP packets
    for message in message_list:
        packet = doip_layer / message
        print(bytes(packet))
        sock.send(bytes(packet))
finally:
    print('closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()