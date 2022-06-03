import hashlib
import socket as s


def create_socket_hash(socket: s.socket) -> str:
    m = hashlib.md5()
    addr, port = socket.getpeername()
    m.update(addr.encode())
    m.update(str(port).encode())
    return m.hexdigest()


def create_socket_hash_with(addr: str, port: int) -> str:
    m = hashlib.md5()
    m.update(addr.encode())
    m.update(str(port).encode())
    return m.hexdigest()
