import hashlib


def create_socket_hash(socket):
    m = hashlib.md5()
    addr, port = socket.getpeername()
    m.update(addr.encode())
    m.update(str(port).encode())
    return m.hexdigest()


def create_socket_hash_with(addr, port):
    m = hashlib.md5()
    m.update(addr.encode())
    m.update(str(port).encode())
    return m.hexdigest()
