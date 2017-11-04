"""
項目27: プライベート属性よりパブリック属性が好ましい
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec28_collections import *


class TestIndexableNode(unittest.TestCase):
    """
    シーケンス的な アクセスのできる二分木構造
    """

    def test_sequence(self):
        """
        様々なデータアクセスをテストする
        """
        tree = IndexableNode(
            10,
            left=IndexableNode(
                5,
                left=IndexableNode(2),
                right=IndexableNode(
                    6, right=IndexableNode(7))),
            right=IndexableNode(
                15, left=IndexableNode(11)))

        self.assertEqual(tree.left.right.right.value, 7)
        self.assertEqual(tree[0], 2)
        self.assertEqual(tree[1], 5)
        self.assertEqual(list(tree), [2, 5, 6, 7, 10, 11, 15])


class TestSequenceNode(unittest.TestCase):

    def test_len(self):
        """
        長さなどに対応できるようにする
        """
        tree = SequenceNode(
            10,
            left=SequenceNode(
                5,
                left=SequenceNode(2),
                right=SequenceNode(
                    6, right=SequenceNode(7))),
            right=SequenceNode(
                15, left=SequenceNode(11)))

        self.assertEqual(len(tree), 7)


class TestBetterNode(unittest.TestCase):

    def test_index(self):
        """
        index関数でアクセスできるかをテスト
        """
        tree = BetterNode(
            10,
            left=BetterNode(
                5,
                left=BetterNode(2),
                right=BetterNode(
                    6, right=BetterNode(7))),
            right=BetterNode(
                15, left=BetterNode(11)))

        self.assertEqual(tree.index(7), 3)


if __name__ == '__main__':
    unittest.main()
