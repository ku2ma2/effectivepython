"""
項目19: キーワード引数でオプションの振る舞いを表すのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec19_keyword_arguments import *


class TestPositionalArguments(unittest.TestCase):
    """
    剰余を計算する
    """

    def test_default_successful(self):
        """
        通常の使い方を数種類比較する
        """
        expected = 6

        self.assertEqual(remainder(20, 7), expected)
        self.assertEqual(remainder(20, division=7), expected)
        self.assertEqual(remainder(division=7, number=20), expected)


if __name__ == '__main__':
    unittest.main()
