"""
項目22: 辞書やタプルで記録管理するよりもヘルパークラスを使うのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec23_callable_class import *


class TestCountMissing(unittest.TestCase):
    """
    内部カウンタインターフェースのテスト
    """

    def test_countup(self):
        """
        呼び出されるたびに クラス変数 added が上がっていく(インクリメントされる)。
        """
        counter = CountMissing()
        counter()
        actual = counter.added
        expected = 1
        self.assertEqual(actual, expected)

        # 再度カウントアップすると2になる
        counter()
        actual = counter.added
        expected = 2
        self.assertEqual(actual, expected)

    def test_callable(self):
        """
        クラスメソッドを関数のように呼べるかどうかの確認 __call__
        """
        counter = CountMissing()
        self.assertTrue(callable(counter))


if __name__ == '__main__':
    unittest.main()
