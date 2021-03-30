from uds.enum.service_id import ServiceID
from uds.pdu.base import ServiceBase

class Authentication(ServiceBase):
    """
    Authenticate tester on ECU with either PKI certificate exchange or with
    challenge response.

    Authentication allows a tester to access restricted data or services that
    could lead to sensitive operations.

    Difference to security access is that an ACL can be managed with authentication
    and user role are assigned to authenticated certificate that will give access
    to only a subset of services/data.

    Switch of session let the user authenticated so deauthentication need to be
    done explicitly. 

    NB: Autosar only implements the authentication via PKI certificate, 
    challenge-response is out of scope of AUTOSAR.
    """

    __slots__ = ('sub_function',) # Space saving + faster access (good for a fuzzer so)

    SERVICE_ID  = ServiceID.AUTHENTICATION
    
    def __init__(self, sub_function = 0x0): 
        self.sub_function = sub_function

    def __bytes__(self):
        pass