import time
from enum import IntFlag

from protocols.uds.transport.ethernet.enum.connection_kind import ConnectionKind
from protocols.uds.transport.ethernet.payload.routing_activation import RoutingActivationRequest

class EthernetClient(object):
    """
    Defines an ethernet client for DoIP protocol.

    DoIP works with a state machine that will check if everything is
    correctly initialized and set before processing some request.

    Some behavior will close socket and so communication need to be
    re-established in purpose to pursue test session.
    
    tcp_data : Socket used for data exchange with ECU (TCP)
    udp_discovery: Socket used for discovery of ECU (UDP)

    ISO 13400 defines which messages should be sent over tcp_data or 
    udp_discovery.
    """
    DEFAULT_PORT    = 13400
    TCP_SECURE_PORT = 3496

    class DoIPState(IntFlag):
        """
        Enumerates DoIP states used for state machine during UDS communication
        with sensor. Some behavior will require to retrigger routing activation
        or reopen socket because sockets can be closed by remote ECU.

        This ensure that before processing next request ECU is in correct state.

        ISO 13400 defines in which conditions routing activation/socket opening
        should be done again. 
        """
        NOT_READY     = 0x00
        SOCKET_OPENED = 0x01
        ROUTED        = 0x02

    def __init__(self, secure = False, routing_activation_request = RoutingActivationRequest(), tester_present_delay = 2):
        """
        Constructs a new instance.
        
        :param      secure:                      Define if TCP secure (TLS) should be used
        :type       secure:                      bool
        :param      routing_activation_request:  Define which routing activation request should be used (can be OEM specific)
        :type       routing_activation_request:  RoutingActivationRequest
        :param      tester_present_delay:        Define timer delay (in seccond) between request sent, if delay is reached then tester present is sent.
        :type       tester_present_delay:        int
        """

        # Set client to not ready so we know socket needs to be opened.
        self._state                          = DoIPState.NOT_READY
        
        self._tcp_data                       = None
        self._udp_discovery                  = None
        
        self.secure                          = secure 
        
        self.routing_activation_oem_specific = routing_activation_request
        self.tester_present _delay           = tester_present_delay
        self.next_tester_present_timestamp   = time.time() + self.tester_present_delay

    def _create_socket(self):
        """
        Creates sockets required for DoIP exchange with ECU.
        """
        # TODO: Handle secure TCP data
        if self.secure:    
            pass

        self._tcp_data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Disable TCP delay (Nagle's algorithm) to send single TCP packet, it's less efficient
        # with small packets and high traffic but might be required for some equipment.
        # Furthermore large file can be sent more efficiently with Nagle's off.
        self._tcp_data.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self._tcp_data.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self._tcp_data.settimeout(self.SOCKET_TIMEOUT)

        self._udp_discovery = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp_discovery.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._udp_discovery.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def _await_announcement(self):
        pass

    def vehicle_identification(self, eid = None, vin = None):
        pass

    def routing_activation(self):
        """
        Routes tester address into ECU and enable further UDS requests.        
        """
        pass

    def send(self, message):
        """
        { function_description }
        
        :param      message:  The message
        :type       message:  { type_description }
        """
        pass

    def receive(self):
        pass