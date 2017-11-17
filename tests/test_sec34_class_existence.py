"""
項目32: 遅延属性には __getattr__, __getattribute__, __setattr__ を使う
"""

import sys
import os
import unittest
from io import StringIO

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec34_class_existence import *


class TestPoint2D(unittest.TestCase):
    """
    ２次元の座標情報を表す
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_serialize(self):
        """
        JSON情報のテスト
        """
        point = Point2D(5, 3)
        self.assertEqual(point.serialize(), '{"args": [5, 3]}')

    def test_repr(self):

        point = Point2D(5, 3)
        print(point)
        expected = 'Point2D(5, 3)\n'

        self.assertEqual(self.captor.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
