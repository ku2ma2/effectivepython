"""
項目27: プライベート属性よりパブリック属性が好ましい

Prefer Public Attributes Over Private Ones

- プライベート属性は、Pythonが厳密に強制しているわけじゃない
- サブクラスを締め出すのではなく、内部APIと属性を利用できるように想定をしておく
- プライベート属性としてアクセスを制御するのは避け、保護フィールドについてドキュメンテーションで説明
- プライベート属性は、コントロール外のサブクラスによる名前衝突を避けるために利用

### とはいえ

- Python使いが「大人」だとは言え名前衝突の判断基準はどうしているのだろうか
- 属性という風に表現するのには意味があるんだな。インスタンス変数は共有するためのものという扱い

"""


class ApiClass(object):
    """
    親クラス
    """

    def __init__(self):
        """ コンストラクタで仮の属性を設定する
        """
        self.__value = 5

    def get(self):
        """ プライベート属性を返す
        """
        return self.__value


class ChildClass(ApiClass):
    """
    サブクラス
    """

    def __init__(self):
        super().__init__()
        self._value = 'hello'


if __name__ == "__main__":
    pass
