"""
項目26: 多重継承は mix-in ユーティリティクラスだけに使う
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec26_mixin import *


class TestToDictMixin(unittest.TestCase):
    """
    Pythonオブジェクトを辞書表現にシリアライズのテスト
    """

    def test_binary_tree(self):
        """
        二分木を作ってみる
        """
        tree = BinaryTree(10,
                          left=BinaryTree(7, right=BinaryTree(9)),
                          right=BinaryTree(13, left=BinaryTree(11)))
        expected = {'left': {'left': None,
                             'right': {'left': None, 'right': None, 'value': 9},
                             'value': 7},
                    'right': {'left': {'left': None, 'right': None, 'value': 11},
                              'right': None,
                              'value': 13},
                    'value': 10}
        self.assertEqual(tree.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
