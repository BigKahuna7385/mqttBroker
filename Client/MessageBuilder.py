from Client.HeaderBuilder import HeaderRepo


class MessageBuilder:
    def __init__(self):
        self._header_type = None
        self._message = None

        def header(header_type):
            self._header_type = HeaderRepo.get_header(header_type)
        def message(message):
            self._message = message
        def build():
            header = HeaderRepo.build_header(get_header_type(),get_message())

        def get_header_type():
            return self._header_type

        def get_message():
            return self._message