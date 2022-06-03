from unittest import TestCase

from Utils.HeaderBuilder import HeaderBuilder
from Utils.MessageParser import MessageParser


class TestHeaderBuilder(TestCase):
    def test_build_header(self):
        header_builder = HeaderBuilder()
        header = header_builder.build_header("CONNECT", "", "a/b")
        self.assertEqual(header, b'\x10\x05\x00\x03a/b')

    def test_get_type_code_from_byte(self):
        message_parser = MessageParser()
        self.assertEqual(message_parser.parse_fixed_header(b'\x10\x05\x00\x03a/b'), "CONNECT")
