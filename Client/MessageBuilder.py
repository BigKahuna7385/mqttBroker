from Client.HeaderBuilder import HeaderBuilder


class MessageBuilder:
    def __init__(self):
        self._header_type = None
        self._message = None
        self.header_builder = HeaderBuilder()

        def header(header_type):
            self._header_type = self.header_builder.build_header(header_type)

        def message(message):
            self._message = message

        def build():
            self.header = self.header_builder.build_header(get_header_type(), get_message())

        def get_header_type():
            return self._header_type

        def get_message():
            return self._message
