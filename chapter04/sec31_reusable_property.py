"""
項目31: ディスクリプタを使って @property デコレータのメソッドを再利用可能にする

Use Descriptors for Reusable @property Methods

- ディスクリプタを定義して、@property メソッドの振る舞いや確認作業を再利用する
- WeakKeyDirectoryを用いて、ディスクリプタクラスがメモリリークを起こさないようにする
- __getattribute__ がディスクリプタプロトコルをどのように使って属性の取得や設定を行なっているか、正確に把握しようとして立ち往生をしない。

### 所感

- 実際は、ここのGradeの所のメモリリークまで考えが至らない気がする。
- 便利そうだけど思い出せるかな…
- https://qiita.com/pashango2/items/fb1e5e79589279c5a861

"""

from weakref import WeakKeyDictionary


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
        成績評価のセッター
        100点満点のテストなので0〜100以内である事を保証する
        """
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

        self._grade = value


class Grade(object):
    def __init__(self):
        """
        コンストラクタ
        WeakKeyDictionaryを使って実行時にプログラムでインスタンスの
        最後に残っている参照が、その辞書のキー集合で保持されているのだけだと
        分かったら利用されているオブジェクトから削除する
        """
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        """
        Grede内の属性に代入
        辞書 _values の中から instance の名前で取得
        """
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        """
        Grede内の属性を取得
        辞書 _values の中から instance の名前で設定
        代入する value が 0 〜 100 でなければ ValueError
        """
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


if __name__ == "__main__":
    pass
