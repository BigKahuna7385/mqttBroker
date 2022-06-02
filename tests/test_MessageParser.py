from unittest import TestCase

from Utils.MessageParser import MessageParser


class TestMessageParser(TestCase):
    def test_parse_fixed_header(self):
        message_parser = MessageParser()
        message = b'\x00\x03\x00\x00\x00\x1a\x00\x00\x00\x03a/b"Dies ist ein Test"'
        header_type = message_parser.parse_fixed_header(message)
        self.assertEqual(header_type, "PUBLISH")

