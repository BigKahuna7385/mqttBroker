from unittest import TestCase

from HeaderBuilder import HeaderRepo


class TestHeaderBuilder(TestCase):
    def test_build_header(self):
        header_repo = HeaderRepo()
        header = header_repo.build_header("CONNECT", "HALLO")
        self.assertEqual(header, "0001000000000101")
