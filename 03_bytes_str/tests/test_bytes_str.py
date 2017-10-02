"""
項目3: bytes,str,unicodeの違いを知っておくのテスト
"""

import unittest

from bytes_str import to_str


class TestBytesStr(unittest.TestCase):
    """
    Stringへの変換
    """

    def test_to_str_str型だった場合str型がそのまま返える(self):
        """
        str型だった場合str型がそのまま返える
        """
        actual = isinstance(to_str('string'), str)
        self.assertTrue(actual)

    def test_to_str_バイナリだった場合str型に変換して返す(self):
        """
        バイナリだった場合str型に変換して返す
        """
        expected = 'binary'
        actual = isinstance(to_str(b'binary'), str)
        self.assertTrue(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
