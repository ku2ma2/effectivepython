"""
項目20: 動的なデフォルト引数を指定するときはNoneとdocstringsを使うのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter02')

from sec21_keyword_only_arguments import *


class TestKeyworOnlyArguments(unittest.TestCase):
    """
    ログを出力する
    """

    def test_ignore_overflow(self):
        """
        ignore_overflow が True ならば 0 を返す
        """
        expected = 0
        actual = safe_division(1.0, 10**500,
                               ignore_overflow=True,
                               ignore_zero_division=False)

        self.assertEqual(actual, expected)

    def test_ignore_zero_division(self):
        """
        ignore_zero_division が True ならば inf(無限大) を返す
        """
        expected = float('inf')
        actual = safe_division(1.0, 0,
                               ignore_overflow=False,
                               ignore_zero_division=True)

        self.assertEqual(actual, expected)

    def test_keyword_arguments_type_error(self):
        """ 
        キーワード引数を呼び出し元で設定しないとエラー
        """
        with self.assertRaises(TypeError):
            safe_division(1.0, 0, False, True)


if __name__ == '__main__':
    unittest.main()
