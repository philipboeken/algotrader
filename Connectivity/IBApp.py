from Connectivity import IBClient
from Connectivity import IBWrapper
from threading import Thread


class IBApp(IBWrapper, IBClient):
    def __init__(self, ipaddress, portid, clientid):
        IBWrapper.__init__(self)
        IBClient.__init__(self, wrapper=self)

        self.connect(ipaddress, portid, clientid)

        thread = Thread(target=self.run)
        thread.start()

        setattr(self, "_thread", thread)

        self.init_error()
