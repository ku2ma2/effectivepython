"""
項目32: 遅延属性には __getattr__, __getattribute__, __setattr__ を使う
"""

import sys
import os
import unittest
from io import StringIO

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec35_class_attributes import *


class TestBetterCustomer(unittest.TestCase):
    """
    ２次元の座標情報を表す
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_attributes(self):
        """
        属性の設定テスト
        """

        foo = BetterCustomer()
        print('Before:', repr(foo.first_name), foo.__dict__)
        foo.first_name = 'Euclid'
        print('After:', repr(foo.first_name), foo.__dict__)

        expected = 'Before: \'\' {}\n'
        expected += 'After: \'Euclid\' {\'_first_name\': \'Euclid\'}\n'

        self.assertEqual(self.captor.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
