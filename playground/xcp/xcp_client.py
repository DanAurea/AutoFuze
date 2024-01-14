import enum
import socket
import sys
import time

# Scapy is used for ease of testing Wireshark dissector but could be replaced with internal library once the dissector is completed
from scapy.contrib.automotive.xcp.xcp import XCPOnTCP , XCPOnUDP, CTORequest
from scapy.contrib.automotive.xcp.cto_commands_master import *
from scapy.layers.inet import IP

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5555)
print('connecting to %s port %s' % server_address)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(server_address)
sock.settimeout(2)

try:
    command_master_list = [
                                Connect, Disconnect, GetStatus, Synch, GetCommModeInfo, GetId,
                                SetRequest, GetSeed, Unlock, SetMta, Upload, ShortUpload,
                                BuildChecksum, TransportLayerCmd, TransportLayerCmdGetSlaveId,
                                TransportLayerCmdGetDAQId, TransportLayerCmdSetDAQId, UserCmd,
                                Download, DownloadNext, DownloadMax, ShortDownload, ModifyBits,
                                SetCalPage, GetCalPage, GetPagProcessorInfo, GetSegmentInfo,
                                GetPageInfo, SetSegmentMode, GetSegmentMode, CopyCalPage, SetDaqPtr,
                                WriteDaq, SetDaqListMode, GetDaqListMode, StartStopDaqList, StartStopSynch,
                                ReadDaq, GetDaqClock, GetDaqProcessorInfo, GetDaqResolutionInfo, 
                                GetDaqListInfo, GetDaqEventInfo, ClearDaqList, FreeDaq, AllocDaq,
                                AllocOdt, AllocOdtEntry, ProgramStart, ProgramClear, Program, ProgramReset,
                                GetPgmProcessorInfo, GetSectorInfo, ProgramPrepare, ProgramFormat, ProgramNext,
                                ProgramMax, ProgramVerify
                            ]

    for cmd in command_master_list:
        sock.send(bytes(XCPOnTCP() / CTORequest() / cmd())[20:])
finally:
    print('closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()