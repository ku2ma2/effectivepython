"""
項目29: getやsetメソッドよりもの素のままの属性を使う
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec29_plain_attributes import *


class TestResistor(unittest.TestCase):
    """
    抵抗器
    """

    def test_init(self):
        """
        コンストラクタの属性設定テスト
        """

        r1 = Resistor(50e3)
        r1.ohms = 10e3
        actual = r1.ohms
        expected = 10000.0
        self.assertEqual(actual, expected)


class TestVoltageResistance(unittest.TestCase):
    """
    抵抗器のボルト計算
    """

    def test_amps(self):
        """
        アンペア計算
        """

        r2 = VoltageResistance(1e3)
        actual = r2.current
        expected = 0
        self.assertEqual(actual, expected)

        r2.voltage = 10  # ボルトを10に下げると currentも変更されるのを確認する
        actual = r2.current
        expected = 0.01
        self.assertEqual(actual, expected)


class TestBoundedResistance(unittest.TestCase):
    """
    抵抗器のオーム計算
    """

    def test_zero_value_error(self):
        """
        アンペア計算0だとvalueerror
        """
        with self.assertRaises(ValueError):
            r3 = BoundedResistance(1e3)
            r3.ohms = 0

    def test_invalid_value_error(self):
        """
        アンペア計算 不当な値 でも valueerror
        """
        with self.assertRaises(ValueError):
            r3 = BoundedResistance(-3)


class TestFixedResistance(unittest.TestCase):
    """
    抵抗器のオーム計算
    """

    def test_zero_value_error(self):
        """
        属性は必ずインスタンスで設定されるものなので
        その後に代入しようとすると AttributeError
        """
        with self.assertRaises(AttributeError):
            r4 = FixedResistance(1e3)
            r4.ohms = 2e3


if __name__ == '__main__':
    unittest.main()
