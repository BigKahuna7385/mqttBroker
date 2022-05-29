class Subscriber:
    def __init__(self, client_id, ip_address, port):
        _client_id = client_id
        _ip_address = ip_address
        _port = port

        def get_ip_address():
            return _ip_address

        def get_port():
            return _port

        def get_client_id():
            return _client_id