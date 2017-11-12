"""
項目32: 遅延属性には __getattr__, __getattribute__, __setattr__ を使う
"""

import sys
import os
import unittest
from io import StringIO

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec32_lazy_attributes import *


class TestLazyDB(unittest.TestCase):
    """
    DBの行(row)をPythonオブジェクトで表現する
    """

    def test_property(self):
        """
        属性テスト
        """
        data = LazyDB()
        self.assertEqual(data.__dict__, {'exists': 5})
        self.assertEqual(data.foo, 'Value for foo')
        self.assertEqual(data.__dict__, {'exists': 5, 'foo': 'Value for foo'})


class TestLoggingLazyDB(unittest.TestCase):
    """
    いつ __getattr__ が呼ばれたかのためにログ出力する
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_property(self):
        """
        属性テスト
        """
        data = LoggingLazyDB()
        self.assertEqual(data.exists, 5)

        # 2回の data.foo 参照で最初だけ __getattr__ が呼び出されるのを確認
        print('foo:', data.foo)
        print('foo:', data.foo)

        expected = 'Called __getattr__(foo)\n'
        expected += 'foo: Value for foo\n'
        expected += 'foo: Value for foo\n'

        self.assertEqual(self.captor.getvalue(), expected)


class TestValidatingDB(unittest.TestCase):
    """
    データベーストランザクションを想定した属性設定のパターン
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_getattribute(self):
        """
        属性の取得経緯を表示
        """

        data = ValidatingDB()
        print('exists:', data.exists)
        print('foo:', data.foo)
        print('foo:', data.foo)

        expected = 'Called __getattribute__(exists)\n'
        expected += 'exists: 5\n'
        expected += 'Called __getattribute__(foo)\n'
        expected += 'foo: Value for foo\n'
        expected += 'Called __getattribute__(foo)\n'
        expected += 'foo: Value for foo\n'

        self.assertEqual(self.captor.getvalue(), expected)


class TestLoggingSavingDB(unittest.TestCase):
    """
    ロギングを追加したDBデータ追加処理
    """

    def setUp(self):
        self.captor = StringIO()
        sys.stdout = self.captor

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_setattr(self):
        """
        属性設定されるごとに処理される __setattr__テスト
        """

        data = LoggingSavingDB()
        print('Before:', data.__dict__)
        data.foo = 5
        print('After:', data.__dict__)
        data.foo = 7
        print('Finally:', data.__dict__)

        expected = 'Before: {}\n'
        expected += 'Called __setattr__(foo, 5)\n'
        expected += 'After: {\'foo\': 5}\n'
        expected += 'Called __setattr__(foo, 7)\n'
        expected += 'Finally: {\'foo\': 7}\n'

        self.assertEqual(self.captor.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
