"""
項目3: bytes,str,unicodeの違いを知っておくのテスト
"""

import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


from urllib.parse import parse_qs
from io import StringIO

from helper_url import *


class TestGetFirstInt(unittest.TestCase):
    """
    辞書でデフォルト値を指定して取得する
    """

    def test_find_key(self):
        """
        キー(key)が見つかった場合はその値を返す
        """
        data = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
        expected = 5
        actual = get_first_int(data, 'red')

        self.assertEqual(actual, expected)

    def test_not_found_key(self):
        """
        キー(key)が見つからなかった場合はデフォルト値を返す
        """
        data = data = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
        expected = 3
        actual = get_first_int(data, 'green', 3)

        self.assertEqual(actual, expected)

    def test_set_default_value(self):
        """
        キーが見つからなかった場合のデフォルト値を与えない場合は0が返ってくる
        """
        data = data = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
        expected = 0
        actual = get_first_int(data, 'opacity')

        self.assertEqual(actual, expected)


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

        expected = """Red: 5
Green: 0
Opacity: 0
"""
        main()
        self.assertEqual(self.captor.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
