from Broker.utils import create_socket_hash_with


class Subscriber:
    def __init__(self, ip_address, port):
        self._client_id = create_socket_hash_with(ip_address, str(port))
        self._ip_address = ip_address
        self._port = port

    def get_ip_address(self):
        return self._ip_address

    def get_port(self):
        return self._port

    def get_client_id(self):
        return self._client_id
