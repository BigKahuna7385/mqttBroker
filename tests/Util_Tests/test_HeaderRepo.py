from unittest import TestCase

from Utils.HeaderBuilder import HeaderBuilder


class TestHeaderBuilder(TestCase):
    def test_build_header(self):
        header_builder = HeaderBuilder()
        header = header_builder.build_header("CONNECT", "HALLO")
        self.assertEqual(header, "0001000000000101")

    def test_get_type_code_from_byte(self):
        header_builder = HeaderBuilder()
        self.assertEqual(header_builder.get_header_type_from(b"\x00\x03"), "PUBLISH")
