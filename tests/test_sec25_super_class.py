"""
項目25: 親クラスをsuperを使って初期化する
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec25_super_class import *


class TestMyBaseClass(unittest.TestCase):
    """
    super表記で引数を省略できるかどうかのテスト
    """

    def test_assert_super(self):
        """
        内容は同じだが表記の違うsuperで同じ結果になるかどうかのテスト
        """
        actual = Explicit(10).value
        expected = Implicit(10).value
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
