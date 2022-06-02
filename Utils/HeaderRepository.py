class HeaderRepository:
    def __init__(self):
        self._type_dict = {
            "CONNECT": "0x1",
            "CONNACK": "0x2",
            "PUBLISH": "0x3",
            "PUBREC": "0x4",
            "PUBREL": "0x5",
            "PUBCOMP": "0x6",
            "SUBSCRIBE": "0x7",
            "SUBACK": "0x8",
            "UNSUBSCRIBE": "0x9",
            "UNSUBACK": "0xA",
            "PINGREQ": "0xB",
            "PINGRESP": "0xC",
            "DISCONNECT": "0xD",
            "AUTH": "0xE"
        }

        self._flags_dict = {
            "CONNECT": "0x0",
            "CONNACK": "0x0",
            "PUBLISH": "0x0",
            "PUBREC": "0x0",
            "PUBREL": "0x2",
            "PUBCOMP": "0x0",
            "SUBSCRIBE": "0x2",
            "SUBACK": "0x0",
            "UNSUBSCRIBE": "0x2",
            "UNSUBACK": "0x0",
            "PINGREQ": "0x0",
            "PINGRESP": "0x0",
            "DISCONNECT": "0x0",
            "AUTH": "0x0"
        }

        self._reversed_type_dict = {
            "0001": "CONNECT",
            "0002": "CONNACK",
            "0003": "PUBLISH",
            "0004": "PUBREC",
            "0005": "PUBREL",
            "0006": "PUBCOMP",
            "0007": "SUBSCRIBE",
            "0008": "SUBACK",
            "0009": "UNSUBSCRIBE",
            "000A": "UNSUBACK",
            "000B": "PINGREQ",
            "000C": "PINGRESP",
            "000D": "DISCONNECT",
            "000E": "AUTH"
        }

    def get_flag(self, header_type):
        return self._flags_dict[header_type]

    def get_type(self, header_type):
        return self._type_dict[header_type]

    def get_type_from(self, byte_code):
        return self._reversed_type_dict[byte_code.hex()]
