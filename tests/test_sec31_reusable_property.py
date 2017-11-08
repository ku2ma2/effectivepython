"""
項目31: ディスクリプタを使って @property デコレータのメソッドを再利用可能にする
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter04')

from sec31_reusable_property import *


class TestHomework(unittest.TestCase):
    """
    宿題テスト
    """

    def test_set_property(self):
        """
        セッターゲッターテスト
        """
        galileo = Homework()
        galileo.grade = 95

        actual = galileo.grade
        expected = 95

        self.assertEqual(actual, expected)

    def test_valueerror_property(self):
        """
        属性に 0 ~ 100 以内では無い値を代入すると ValueError
        """
        with self.assertRaises(ValueError):
            galileo = Homework()
            galileo.grade = 101


class TestExam(unittest.TestCase):
    """
    試験(Exam)のテスト
    """

    def test_property_in_grade(self):
        """
        Gradeに各属性の設定ができるかのテスト
        """
        first_exam = Exam()
        first_exam.writing_grade = 82
        second_exam = Exam()
        second_exam.writing_grade = 75

        self.assertEqual(first_exam.writing_grade, 82)
        self.assertEqual(second_exam.writing_grade, 75)

    def test_valueerror_in_grade(self):
        """
        Grade の 0 〜 100以内では無い属性を入れると ValueError
        """
        with self.assertRaises(ValueError):
            exam = Exam()
            exam.writing_grade = 101


if __name__ == '__main__':
    unittest.main()
