import socket as s

from Broker.utils import create_socket_hash_with


class Subscriber:
    def __init__(self, socket: s.socket):
        self._ip_address = socket.getpeername()[0]
        self._port = socket.getpeername()[1]
        self._client_id = create_socket_hash_with(self._ip_address, str(self._port))
        self._socket = socket

    def get_socket(self) -> s.socket:
        return self._socket

    def get_ip_address(self) -> str:
        return self._ip_address

    def get_port(self) -> int:
        return self._port

    def get_client_id(self) -> str:
        return self._client_id
