"""
項目16: リストを返さずにジェネレータを返すことを考えるのテスト
"""

import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec16_consider_generator import *


class TestIndexWorsIter(unittest.TestCase):
    """
    英文文字列(単語がスペースで区切られている)の各単語の位置をイテレータで返す
    """

    def test_success(self):
        """
        成功パターン
        """
        it = index_word_iter('Four score and seven years')
        actual = list(it)

        expected = [0, 5, 11, 15, 21]

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
