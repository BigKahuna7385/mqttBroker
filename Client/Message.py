import json

from Client.HeaderBuilder import HeaderBuilder


class Message:
    def __init__(self, header_type, payload):
        self._header_type = header_type
        self._payload = payload
        self.header_builder = HeaderBuilder()

    def build(self):
        return self.header_builder.build_header(self._header_type, self._payload) + json.dumps(self._payload)
