import enum
import socket
import sys
import time

sys.path.append("../../protocols")

# Scapy is used for ease of testing Wireshark dissector but could be replaced with internal library once the dissector is completed
from scapy.contrib.automotive.xcp.xcp import XCPOnTCP , XCPOnUDP, CTORequest, CTOResponse
from scapy.contrib.automotive.xcp.cto_commands_slave import *
from scapy.layers.inet import IP

from xcp.pdu.command import *
from xcp.transport.ethernet import EthernetTransport

connect_request = bytes(EthernetTransport()/Connect())

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
                                BuildChecksum, TransportLayerCmd, UserCmd,
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

    command_slave_list = [      
                                GenericResponse, NegativeResponse, EvPacket, ServPacket, TransportLayerCmdGetSlaveIdResponse,
                                TransportLayerCmdGetDAQIdResponse, SegmentInfoMode0PositiveResponse, SegmentInfoMode1PositiveResponse,
                                SegmentInfoMode2PositiveResponse, ConnectPositiveResponse, StatusPositiveResponse, CommonModeInfoPositiveResponse,
                                IdPositiveResponse, SeedPositiveResponse, UnlockPositiveResponse, UploadPositiveResponse, ShortUploadPositiveResponse,
                                ChecksumPositiveResponse, CalPagePositiveResponse, PagProcessorInfoPositiveResponse, PageInfoPositiveResponse,
                                SegmentModePositiveResponse, DAQListModePositiveResponse, StartStopDAQListPositiveResponse, DAQClockListPositiveResponse,
                                ReadDAQPositiveResponse, DAQProcessorInfoPositiveResponse, DAQResolutionInfoPositiveResponse, DAQListInfoPositiveResponse,
                                DAQEventInfoPositiveResponse, ProgramStartPositiveResponse, PgmProcessorPositiveResponse, SectorInfoPositiveResponse
                            ]

    for cmd in command_master_list:
        if cmd == GetDaqListMode:
            print(bytes(cmd()))
        sock.send(bytes(EthernetTransport() / cmd()))

    for cmd in command_slave_list:
        sock.send(bytes(XCPOnTCP() / CTOResponse() / cmd())[20:])
finally:
    print('closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()