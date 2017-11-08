"""
項目30: 属性をリファクタリングする代わりに @property を考える
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec30_consider_property import *


class TestBucket(unittest.TestCase):
    """
    抵抗器
    """

    def test_deduct(self):
        """
        バケツクエスト
        """

        bucket = Bucket(period=60)
        self.assertEqual(
            str(bucket), 'Bucket(max_quota=0, quota_consumed=0)')
        fill(bucket, amount=100)

        self.assertEqual(
            str(bucket), 'Bucket(max_quota=100, quota_consumed=0)')
        self.assertTrue(deduct(bucket, 99))
        self.assertEqual(
            str(bucket), 'Bucket(max_quota=100, quota_consumed=99)')
        self.assertFalse(deduct(bucket, 3))
        self.assertEqual(
            str(bucket), 'Bucket(max_quota=100, quota_consumed=99)')


if __name__ == '__main__':
    unittest.main()
