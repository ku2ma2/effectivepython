"""
項目23: クラス型ではなく関数型で単純なインターフェースでシンプルに

Accept Functions for Simple Interfaces Instead of Classes

- コンポーネント間の単純なインターフェースは、大抵インスタンス化せずに関数で済む
- 特殊メソッド __call__ は、インスタンスが通常の関数として呼び出される事を可能にする
- 状態をもつクロージャを定義する代わりに __call__ メソッドを提供することを考える

"""


class CountMissing(object):
    """
    内部カウントをするためのクラス
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.added = 0

    def __call__(self):
        """
        関数として呼ばれた場合の処理
        added をインクリメントする

        >>> counter = CountMissing()
        >>> counter()
        0
        >>> counter.added
        1
        >>> counter()
        0
        >>> counter.added
        2
        """
        self.added += 1
        return 0


if __name__ == "__main__":
    pass
