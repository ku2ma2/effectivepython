"""
項目18: 可変長位置引数を使って見た目をすっきりさせるのテスト
"""

import sys
import os
import unittest
from io import StringIO

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec18_positional_arguments import *


class TestPositionalArguments(unittest.TestCase):
    """
    ログメッセージを表示する
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_arg(self):
        """
        オプションリスト values を message のあとに追加して表示する
        """
        actual = log_with_arg('My numbers are', 1, 2)
        expected = 'My numbers are: 1, 2\n'

        self.assertEqual(self.captor.getvalue(), expected)

    def test_no_arg(self):
        """
        オプションリスト values がない場合はそのまま message を表示する
        """
        actual = log_with_arg('Hi there')
        expected = 'Hi there\n'

        self.assertEqual(self.captor.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
