"""
項目11: イテレータを並列に処理するにはzipを使うのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../01')

from sec11_iterator_zip import *


class TestLongestName(unittest.TestCase):
    """
    リスト内の一番長い名前を取得する
    """

    def test_no_default(self):
        """
        通常パターン
        """

        actual = get_longest(['Cecilia', 'Lise', 'Marie'])
        expected = 'Cecilia'

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
