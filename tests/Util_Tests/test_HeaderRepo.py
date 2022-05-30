from unittest import TestCase

from Utils.HeaderBuilder import HeaderBuilder


class TestHeaderBuilder(TestCase):
    def test_build_header(self):
        header_builder = HeaderBuilder()
        header = header_builder.build_header("CONNECT", "HALLO")
        self.assertEqual(header, "0001000000000101")
