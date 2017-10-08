"""
項目8: リスト内包表記は3つ以上の指揮を避けるのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from duplicate_list_comprehension import *


class TestGetFlat(unittest.TestCase):
    """
    入力されたリスト中の数を平方にして返す
    """

    def test_successful(self):
        """
        成功パターン
        """
        input = [[1, 2, 3], [4, 5], [6, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(get_flat(input), expected)


if __name__ == '__main__':
    unittest.main()
