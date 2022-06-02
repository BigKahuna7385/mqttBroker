import hashlib


class Subscriber:
    def __init__(self, ip_address, port):
        self._client_id = str(ip_address).encode() + str(port).encode()
        self._ip_address = ip_address
        self._port = port

    def get_ip_address(self):
        return self._ip_address

    def get_port(self):
        return self._port

    def get_client_id(self):
        return self._client_id
