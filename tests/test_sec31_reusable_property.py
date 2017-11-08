"""
項目31: ディスクリプタを使って @property デコレータのメソッドを再利用可能にする
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec31_reusable_property import *


class TestHomework(unittest.TestCase):
    """
    宿題テスト
    """

    def test_set_property(self):
        """
        セッターゲッターテスト
        """
        galileo = Homework()
        galileo.grade = 95

        actual = galileo.grade
        expected = 95

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
