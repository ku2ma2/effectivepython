"""
項目10: rangeよりはenumerateにするのテスト
"""

import sys
import os
import tempfile
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter01')

from sec10_enumerate_list import *


class TestConvertEnumerate(unittest.TestCase):
    """
    リストを添え字数字つきの辞書にして返す
    """

    def test_no_default(self):
        """
        通常パターン
        """

        expected = [(0, 'one'), (1, 'two'), (2, 'three')]
        actual = convert_enumerate(['one', 'two', 'three'])

        self.assertEqual(actual, expected)

    def test_default(self):
        """
        添え字スタートを設定したパターン
        """

        expected = [(2, 'one'), (3, 'two'), (4, 'three')]
        actual = convert_enumerate(['one', 'two', 'three'], 2)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
