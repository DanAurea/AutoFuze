import sys
sys.path.append("../../")
sys.path.append("../../protocols")

from protocols.xcp.enum.command_code import CalibrationCommandCode
from protocols.xcp.frame import XcpFrame
from protocols.xcp.pdu.command.cal.download import DownloadRequest
from struct import unpack

"""
DISCLAIMER: This only a simple test made as a primary usage of XCP API but more tests should be done in future to ensure good code testability.
"""

data                                            = b"\x00\xf0\xf2\xf2"
download_req                                    = DownloadRequest(number_of_data_element = len(data), alignment = 0x01, data = bytearray(data))

xcp_frame                                       = XcpFrame(packet = download_req)

frame_bytes                                     = bytes(xcp_frame)

command_code, number_of_data_element, alignment = unpack("<3B", frame_bytes[:3])
data_unpack                                     = unpack("<4B", frame_bytes[3:])

assert command_code == CalibrationCommandCode.DOWNLOAD
assert number_of_data_element == len(data)
assert alignment == 0x01
assert bytearray(data) == bytearray(data_unpack)