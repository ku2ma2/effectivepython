"""
項目22: 辞書やタプルで記録管理するよりもヘルパークラスを使うのテスト
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../chapter03')

from sec22_helper_class import *


class TestHelperClassSubject(unittest.TestCase):
    """
    Subjectクラスのテスト
    """

    def test_report_grade_same_weight(self):
        """
        同じ重みつけ(weight)だったばあいは平均になる
        """

        subject = Subject()
        subject.report_grade(score=80, weight=0.10)
        subject.report_grade(score=90, weight=0.10)

        actual = subject.average_grade()
        expected = 85.0
        self.assertEqual(actual, expected)

    def test_report_grade(self):
        """
        違う重み付け(weight)の場合は考慮する
        """

        subject = Subject()
        subject.report_grade(score=60, weight=0.10)
        subject.report_grade(score=100, weight=0.30)

        actual = subject.average_grade()
        expected = 90.0
        self.assertEqual(actual, expected)


class TestHelperClassGradebook(unittest.TestCase):
    """
    Greadebookクラスのテスト
    """

    def test_book(self):
        """
        Math, Englishそれぞれに値を入れて、生徒の平均点を求める
        """

        book = Gradebook()
        albert = book.student('Albert Einstein')
        math = albert.subject('Math')
        math.report_grade(100, 0.30)
        english = albert.subject('English')
        english.report_grade(60, 0.10)

        actual = albert.average_grade()
        expected = 80.0

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
