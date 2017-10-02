"""
項目3: bytes,str,unicodeの違いを知っておくのテスト
"""

import unittest

from bytes_str import to_str, to_bytes


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


if __name__ == '__main__':
    unittest.main()
