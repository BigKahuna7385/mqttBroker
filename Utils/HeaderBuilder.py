from Utils.HeaderRepository import HeaderRepository


class HeaderBuilder:
    def __init__(self):
        self.variable_header = ""
        self._header_repo = HeaderRepository()

    def _get_control_package_type(self, header_type):
        return "{0:04b}".format(int(self._header_repo.get_type(header_type), 16))

    def _get_flag(self, header_type):
        return "{0:04b}".format(int(self._header_repo.get_flag(header_type), 16))

    def _encode_message_length(self, message):
        if len(message) > 255:
            return int(0).to_bytes(1, 'big')
        return len(message).to_bytes(1, 'big')

    def _build_variable_header(self, topic):
        topic_length = len(topic)
        extractor_msb = int("1111111100000000", 2)
        len_msb = topic_length & extractor_msb
        len_msb = len_msb >> 8
        extractor_lsb = int("0000000011111111", 2)
        len_lsb = topic_length & extractor_lsb
        self.variable_header = (len_msb.to_bytes(1, 'big') + len_lsb.to_bytes(1, 'big') + bytes(topic, 'utf-8'))

    def build_header(self, header_type, message, topic):
        if topic:
            self._build_variable_header(topic)
        else:
            self.variable_header = "".encode()

        control_package = self._get_control_package_type(header_type)
        get_flag = self._get_flag(header_type)

        message_length = self._encode_message_length(message.encode('utf-8') + self.variable_header)

        return bitstring_to_bytes(control_package + get_flag) + message_length + self.variable_header


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')


"""
https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901023
MQTT
Control
Packet      Fixed Header flags      Bit 3   Bit 2   Bit 1   Bit 0

CONNECT     Reserved                0       0       0       0
CONNACK     Reserved                0       0       0       0
PUBLISH     Used in MQTT v5.0       DUP         QoS         RETAIN
PUBACK      Reserved                0       0       0       0
PUBREC      Reserved                0       0       0       0
PUBREL      Reserved                0       0       1       0
PUBCOMP     Reserved                0       0       0       0
SUBSCRIBE   Reserved                0       0       1       0
SUBACK      Reserved                0       0       0       0
UNSUBSCRIBE Reserved                0       0       1       0
UNSUBACK    Reserved                0       0       0       0
PINGREQ     Reserved                0       0       0       0
PINGRESP    Reserved                0       0       0       0
DISCONNECT  Reserved                0       0       0       0
AUTH        Reserved                0       0       0       0
"""
