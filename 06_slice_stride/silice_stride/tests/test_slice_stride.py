"""
項目5: シーケンスをどのようにスライスするか知っておくのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from sequence_slice import get_slice


class TestGetSlice(unittest.TestCase):
    """
    スライスの結果を表示する
    """

    def test_successful(self):
        """
        結果をそのまま返す
        """
        dat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.assertEqual(get_slice(dat, ':4'), ['a', 'b', 'c', 'd'])

    def test_not_found_index(self):
        """
        実際にはない 予定より大きなかずの indexの指定
        """
        dat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.assertEqual(get_slice(dat, ':20'), [
                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])


if __name__ == '__main__':
    unittest.main()
