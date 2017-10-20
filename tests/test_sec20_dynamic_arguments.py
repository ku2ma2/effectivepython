"""
項目20: 動的なデフォルト引数を指定するときはNoneとdocstringsを使うのテスト
"""

import sys
import os
import unittest
import freezegun
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec20_dynamic_arguments import *


class TestDynamicArguments(unittest.TestCase):
    """
    ログを出力する
    """

    def test_noarg_when(self):
        """
        whenが設定されていない場合はその時の日時を使う
        freezeを使って日時設定している
        """
        expected = "Hello: 2017-10-20 09:27:31.885687"

        with freezegun.freeze_time('2017-10-20 09:27:31.885687'):
            actual = log_message('Hello')

        self.assertEqual(actual, expected)

    def test_in_when(self):
        """
        whenが設定されていない場合はその時の日時を使う
        freezeを使って日時設定している
        """
        expected = "Hello: 2017-10-20 09:27:32.885687"

        with freezegun.freeze_time('2017-10-20 09:27:32.885687'):
            actual = log_message('Hello', datetime.now())

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
