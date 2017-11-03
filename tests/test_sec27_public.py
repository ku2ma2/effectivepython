"""
項目27: プライベート属性よりパブリック属性が好ましい
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec27_public import *


class TestApiClass(unittest.TestCase):
    """
    Pythonオブジェクトを辞書表現にシリアライズのテスト
    """

    def test_not_equal(self):
        """
        親と子供でクラス属性が違うかを確認する
        """
        child = ChildClass()
        actual = child.get()
        expected = child._value

        self.assertNotEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
