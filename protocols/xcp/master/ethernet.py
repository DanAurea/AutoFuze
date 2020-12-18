from xcp.client.ethernet import EthernetClient
from xcp.master.base import MasterBase

class EthernetMaster(MasterBase):
    """
    This class describes an Ethernet master to communicate easily
    with XCP slave. XCP is working with a Master-Slave model, this
    is a subsidiary class that allow simple communication with
    an ECU.

    If you prefer to send raw packets for fuzzing purpose then using directly
    client should be privilegied.
    """
    def __init__(self):
        self._client             = EthernetClient()
        
    def upload(self):
        pass

    def download(self):
        pass