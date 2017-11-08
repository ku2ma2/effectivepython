"""
項目31: ディスクリプタを使って @property デコレータのメソッドを再利用可能にする

Use Descriptors for Reusable @property Methods

- ディスクリプタを定義して、@property メソッドの振る舞いや確認作業を再利用する
- WeakKeyDirectoryを用いて、ディスクリプタクラスがメモリリークを起こさないようにする
- __getattribute__ がディスクリプタプロトコルをどのように使って属性の取得や設定を行なっているか、正確に把握しようとして立ち往生をしない。

"""


class Homework(object):
    """
    宿題
    """

    def __init__(self):
        """
        コンストラクタ
        成績評価を初期化
        """
        self._grade = 0

    @property
    def grade(self):
        """
        成績評価のゲッター。内部の_gradeを返す
        """
        return self._grade

    @grade.setter
    def grade(self, value):
        """
        成績評価のセッター。0〜100以内出ないとValueError
        """
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

        self._grade = value


class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')


if __name__ == "__main__":
    pass
