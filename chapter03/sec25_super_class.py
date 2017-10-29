"""
項目25: 親クラスをsuperを使って初期化する

Initialize Parent Classes with super

-  Pythonの 標準メソッドの解決順序(MRO)はスーパークラスの初期化順序とダイヤモンド継承の問題を解決する
- 親クラスを初期化するには、常に組み込み関数superを使う

"""


class MyBaseClass(object):
    """
    基底クラス
    """

    def __init__(self, value):
        """ コンストラクタ
        """
        self.value = value


class Explicit(MyBaseClass):
    """
    superを__class__で指定する
    """

    def __init__(self, value):
        """ コンストラクタ
        """
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    """
    superを引数なしで指定する
    """

    def __init__(self, value):
        """ コンストラクタ
        """
        super().__init__(value * 2)


if __name__ == "__main__":
    pass
