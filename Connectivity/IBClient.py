from ibapi.client import EClient
import queue


class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

    def speaking_clock(self):
        print("Getting the time from the server... ")

        time_storage = self.wrapper.init_time()

        self.reqCurrentTime()

        MAX_WAIT_SECONDS = 10

        try:
            current_time = time_storage.get(timeout=MAX_WAIT_SECONDS)
        except queue.Empty:
            print("Exceeded maximum wait for wrapper to respond")
            current_time = None

        while self.wrapper.is_error():
            print(self.get_error())

        return current_time
