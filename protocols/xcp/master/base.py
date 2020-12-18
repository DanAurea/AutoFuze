from xcp.client.base import ClientBase

class MasterBase(object):
    """
    This class describes an abstract Master and shouldn't be
    used without inheritance.

    Master base embed mechanism regarding communication mode used.
    So if a Master child is using interleaved / block mode in some
    situations then this class should provide interoperability between
    different transport layer.
    """

    def __init__(self):
        self._client = ClientBase()
        # Default communication mode is standard.
        # It means only standard mode is available and Master
        # will be able to fetch mode available from slave and
        # inform client of availability of other modes. 
        self.communication_mode = CommModeOptionalBit(0x00)

    def upload(self):
        pass

    def download(self):
        pass