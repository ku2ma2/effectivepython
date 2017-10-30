"""
項目26: 多重継承は mix-in ユーティリティクラスだけに使う

Use Multiple Inheritance Only for Mix-in Utility Classes

- mix-in クラスで同じ結果が得られるなら、多重継承を使うのを止める
- インスタンスレベルでプラグイン可能な振る舞いを使い、mix-in クラスが必要な時に、クラス毎にカスタマイズする
- 単純な振る舞いから複雑な機能を構成するように mix-in を組み合わせて作る

"""


class ToDictMixin(object):
    """
    Mix-in クラス
    Pythonオブジェクトを辞書表現にシリアライズ
    """

    def to_dict(self):
        """ 辞書表現を返す
        """
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        """ 各属性によって辞書表現に対応するように変更
        """
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse_dict(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    """
    二分木の辞書表現
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":
    pass
