from Utils.HeaderRepository import HeaderRepository


class MessageParser:
    def __init__(self):
        self._header_repository = HeaderRepository()

    def parse_fixed_header(self, message):
        first_byte = int.from_bytes(message[:1], "big")
        extractor = int("11110000", 2)
        header_type = (first_byte & extractor) >> 4
        return self._header_repository.get_type_from(header_type)

    def parse_remaining_length(self, message):
        return int.from_bytes(message[1:2], "big")

    def parse_topic(self, data):
        variable_header_start = 2
        data_without_fixed_header = data[variable_header_start:]
        topic_length = self._parse_topic_length(data_without_fixed_header[:2])
        return data_without_fixed_header[variable_header_start:variable_header_start + topic_length]

    def _parse_topic_length(self, topic_length_bytes):
        return int.from_bytes(topic_length_bytes, "big")
