"""
項目3: bytes,str,unicodeの違いを知っておくのテスト
"""

import unittest


class TestBytesStr(unittest.TestCase):
    """
    Stringへの変換
    """

    def test_string(self):
        """
        string型だった場合
        """
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
