import json

from Client.HeaderRepo import HeaderRepo


class Message:
    def __init__(self, header_type, payload):
        self._header_type = header_type
        self._payload = payload



    def build(self):
        return HeaderRepo.get_header(self._header_type) + json.dumps(self._payload)
