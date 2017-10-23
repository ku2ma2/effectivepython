"""
項目22: 辞書やタプルで記録管理するよりもヘルパークラスを使う

Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples

- 大きくネストされた辞書やタプルは再考する
- 完全なクラスの柔軟性が必要となる前は、軽量で変更不能データのコンテナである namedtupleを使う
- 内部の辞書構造が複雑になったらヘルパクラスに分割する
"""
import collections

# namedtuple型
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    """
    科目を表すクラス
    """

    def __init__(self):
        """
        コンストラクタ 点数リストを初期化
        """
        self._grades = []

    def report_grade(self, score, weight):
        """
        点数リストを設定する
        """
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        """
        科目毎に集計をするための処理
        """
        total, total_weight = 0, 0

        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight

        return total / total_weight


class Student(object):
    """
    生徒を表すクラス
    """

    def __init__(self):
        """
        コンストラクタ 科目リストを追加
        """
        self._subjects = {}

    def subject(self, name):
        """
        科目を追加
        """
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        """
        科目の平均点を算出
        """
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1

        return total / count


class Gradebook(object):
    """
    生徒の点数表
    """

    def __init__(self):
        """
        コンストラクタ 生徒リストを追加
        """
        self._students = {}

    def student(self, name):
        """
        生徒を追加
        """
        if name not in self._students:
            self._students[name] = Student()

        return self._students[name]


if __name__ == "__main__":
    pass
