"""
項目17: 引数に対してイテレータを使うときは確実さを尊ぶのテスト
"""

import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec17_defensive_iterator import *


class TestNormalizeDefensive(unittest.TestCase):
    """
    数値リスト numbers の総計と其々の値のパーセンテージをリストにして返す
    """

    def test_success(self):
        """
        成功パターン
        """
        numbers = [15, 35, 80]
        actual = normalize_defensive(numbers)

        expected = [11.538461538461538, 26.923076923076923, 61.53846153846154]

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
