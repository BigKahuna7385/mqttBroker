class HeaderBuilder:
    def __init__(self):
        self.variable_header = ""
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

    def _get_control_package_type(self, header_type):
        return (int(self._type_dict[header_type], 16)).to_bytes(2, 'big')

    def _get_flag(self, header_type):
        return (int(self._flags_dict[header_type], 16)).to_bytes(2, 'big')

    def _encode_message_length(self, message):
        if len(message) > 255:
            return int(0).to_bytes(2, 'big')
        return len(message).to_bytes(2, 'big')

    def _build_variable_header(self, topic):
        topic_length = len(topic)
        extractor_msb = int("1111111100000000", 2)
        len_MSB = topic_length & extractor_msb
        extractor_lsb = int("0000000011111111", 2)
        len_LSB = topic_length & extractor_lsb
        self.variable_header = (len_MSB.to_bytes(2, 'big') + len_LSB.to_bytes(2, 'big') + bytes(topic, 'utf-8'))

    def build_header(self, header_type, message, topic):
        if topic:
            self._build_variable_header(topic)
        else:
            self.variable_header = "".encode()

        control_package = self._get_control_package_type(header_type)
        get_flag = self._get_flag(header_type)

        message_length = self._encode_message_length(message.encode('utf-8') + self.variable_header)

        return control_package + get_flag + message_length + self.variable_header

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
