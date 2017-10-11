"""
項目13: try/except/else/finallyの各ブロックを活用する
"""

import sys
import os
import unittest
import tempfile

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from devide_json import *


class TestDevideJson(unittest.TestCase):
    """
    リスト内の一番長い名前を取得する
    """

    def test_io_error(self):
        """
        ファイルがなかった場合はIOError
        """

        with self.assertRaises(IOError):
            devide_json('not_found_file')

    def test_value_error(self):
        """
        ファイルがJSON形式でなかった場合はValueError
        """

        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""one
two
three
""")
            f.flush()
            with self.assertRaises(ValueError):
                devide_json(f.name)

    def test_zero_division_error(self):
        """
        ファイルがJSON形式ではあるが、値が0だった場合は除算するので
        ZeroDivisionErrorを避けて、空リストが返ってくる
        """

        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""{
    "numerator": 12,
    "denominator": 0
}
""")
            f.flush()
            expected = []
            actual = devide_json(f.name)

        self.assertEqual(actual, expected)

    def test_success(self):
        """
        最終的には計算した結果をrestultとして返す
        """

        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""{
    "numerator": 12,
    "denominator": 2
}
""")
            f.flush()
            expected = 6.0
            actual = devide_json(f.name)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
