"""
項目5: シーケンスをどのようにスライスするか知っておくのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from slice_stride import get_slice_stride


class TestGetSliceStride(unittest.TestCase):
    """
    スライスの結果を表示する
    """

    def test_successful(self):
        """
        結果をそのまま返す
        """
        dat = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

        self.assertEqual(get_slice_stride(dat, '::2'),
                         ['red', 'yellow', 'blue'])
        self.assertEqual(get_slice_stride(dat, '1::2'),
                         ['orange', 'green', 'purple'])


if __name__ == '__main__':
    unittest.main()
