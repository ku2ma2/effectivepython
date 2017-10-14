"""
項目7: mapやfilerの代わりにリスト内包表記を使うのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../01')

from sec07_list_comprehension import *


class TestGetSquare(unittest.TestCase):
    """
    入力されたリスト中の数を平方にして返す
    """

    def test_successful(self):
        """
        成功パターン
        """
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        self.assertEqual(get_square(input), expected)


class TestEvenSquare(unittest.TestCase):
    """
    2で割れる数だけ平方を計算する
    """

    def test_successful(self):
        """
        成功パターン
        """
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [4, 16, 36, 64, 100]

        self.assertEqual(even_square(input), expected)


class TestLenChileName(unittest.TestCase):
    """
    辞書のリスト内包表記
    """

    def test_successful(self):
        """
        成功パターンここでは唐辛子(チリ)の辛さのランク？
        """
        chile_rank = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
        expected = {8, 5, 7}

        self.assertEqual(len_chile_name(chile_rank), expected)


if __name__ == '__main__':
    unittest.main()
