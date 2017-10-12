"""
項目15: クロージャが変数スコープとどう関わるかを知っておくのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from sort_priority import *


class TestSortPriority(unittest.TestCase):
    """
    数をソートするが、一部の数が優先するようにする
    """

    def test_success(self):
        """
        計算した結果をfloatで返す
        """

        numbers = [8, 3, 1, 2, 5, 4, 7, 6]
        group = {2, 3, 5, 7}
        expected = [2, 3, 5, 7, 1, 4, 6, 8]

        actual = sort_priority(numbers, group)

        self.assertEqual(numbers, expected)
        # self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
