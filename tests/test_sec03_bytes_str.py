"""
項目3: bytes,str,unicodeの違いを知っておくのテスト
"""

import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../01')

from io import StringIO

from sec03_bytes_str import *


class TestBytesStr(unittest.TestCase):
    """
    Stringへの変換
    """

    def test_to_str_in_str(self):
        """
        str型だった場合str型がそのまま返える
        """
        actual = isinstance(to_str('string'), str)
        self.assertTrue(actual)

    def test_to_str_in_bytes(self):
        """
        バイナリだった場合str型に変換して返す
        """
        expected = 'bytes'

        to_str_data = to_str(b'bytes')
        actual = isinstance(to_str_data, str)
        self.assertTrue(actual)
        self.assertEqual(to_str_data, expected)


class TestStrBytes(unittest.TestCase):
    """
    バイナリ(bytes)への変換
    """

    def test_to_bytes_in_bytes(self):
        """
        バイナリだった場合そのまま返えす
        """
        actual = isinstance(to_bytes(b'bytes'), bytes)
        self.assertTrue(actual)

    def test_to_bytes_in_str(self):
        """
        バイナリだった場合str型に変換して返す
        """
        expected = b'binary'

        to_bytes_data = to_bytes('binary')
        actual = isinstance(to_bytes_data, bytes)
        self.assertTrue(actual)
        self.assertEqual(to_bytes_data, expected)


class TestMain(unittest.TestCase):
    """
    Main関数の動作テスト
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_main(self):
        """
        Main関数の動作テスト
        """
        main()
        self.assertEqual(self.captor.getvalue(),
                         "<class 'str'>\n<class 'bytes'>\n")


if __name__ == '__main__':
    unittest.main()
