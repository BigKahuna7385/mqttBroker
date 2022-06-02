from Utils.HeaderRepository import HeaderRepository


class MessageParser:
    def __init__(self):
        self._header_repository = HeaderRepository()

    def parse_fixed_header(self, message):
        return self._header_repository.get_type_from(message[:2])
