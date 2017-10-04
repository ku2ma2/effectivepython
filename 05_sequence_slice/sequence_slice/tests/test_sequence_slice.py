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
        self.assertEqual(get_slice(dat, '-4:'), ['e', 'f', 'g', 'h'])
        self.assertEqual(get_slice(dat, '3:-3'), ['d', 'e'])
        self.assertEqual(get_slice(dat, ':'), [
                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.assertEqual(get_slice(dat, ':5'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(get_slice(dat, ':-1'),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.assertEqual(get_slice(dat, '4:'), ['e', 'f', 'g', 'h'])
        self.assertEqual(get_slice(dat, '-3:'), ['f', 'g', 'h'])
        self.assertEqual(get_slice(dat, '2:5'), ['c', 'd', 'e'])
        self.assertEqual(get_slice(dat, '2:-1'), ['c', 'd', 'e', 'f', 'g'])
        self.assertEqual(get_slice(dat, '-3:-1'), ['f', 'g'])

    def test_not_found_index(self):
        """
        実際にはない 予定より大きなかずの indexの指定
        """
        dat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.assertEqual(get_slice(dat, ':20'), [
                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.assertEqual(get_slice(dat, '-20:'),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_over_index(self):
        """
        実際にはない 予定より大きなかずの indexの指定
        """
        dat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.assertEqual(get_slice(dat, ':20'), [
                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        self.assertEqual(get_slice(dat, '-20:'), [
                         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_no_index(self):
        """
        実際にはない 直接の indexの指定をすると IndexError
        """
        dat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        with self.assertRaises(IndexError):
            get_slice(dat, '20')


if __name__ == '__main__':
    unittest.main()
