class Broker:
    def __init__(self, ip_address, port):
        self._ip_address = ip_address
        self._port = port
        # self._needs_auth = False
        # self._username = "Test"
        # self._password = "Test"

    def get_ip_address(self):
        return self._ip_address

    def get_port(self):
        return self._port
