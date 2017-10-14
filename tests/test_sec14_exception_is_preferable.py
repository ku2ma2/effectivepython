"""
項目14: Noneを返すよりは例外を返すのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec14_exception_is_preferable import devide


class TestDevideJson(unittest.TestCase):
    """
    リスト内の一番長い名前を取得する
    """

    def test_value_error(self):
        """
        数値に0が含まれているなどの除算できない数を入力
        した場合はValueError
        """
        with self.assertRaises(ValueError):
            devide(12, 0)

    def test_success(self):
        """
        計算した結果をfloatで返す
        """

        actual = 8.0
        expected = devide(16, 2)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
