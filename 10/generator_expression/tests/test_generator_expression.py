"""
項目7: mapやfilerの代わりにリスト内包表記を使うのテスト
"""

import sys
import os
import tempfile
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from generator_expression import *


class TestLineNumAndSquare(unittest.TestCase):
    """
    入力されたリスト中の数を平方にして返す
    """

    def test_successful(self):
        """
        成功パターン
        """

        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""one
two
three
""")
            f.flush()
            expected = [(3, 9), (3, 9), (5, 25)]
            actual = line_num_and_square(f.name)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
