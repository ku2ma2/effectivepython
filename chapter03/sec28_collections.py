"""
項目28: カスタムコンテナ型はcollections.abcを継承する

Inherit from collections.abc for Custom Container Types

- 単純なユースケースでは(listやdictのような)Pythonのコンテナ型から直接継承をする
- カスタムコンテナ型を正しく実装するには多数のメソッドが必要な事に注意する
- 作ったクラスが必要なインターフェースと振る舞いを備えている事を確かなものにするために
  カスタムコンテナ型はcollections.absで定義されたインターフェースを継承する

"""

from collections.abc import Sequence


class BinaryNode(object):
    """
    二分木のノード表現
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        # (found, count)を返す

        found = None

        if self.left:
            found, count = self.left._search(count, index)

        if not found and count == index:
            found = self
        else:
            count += 1

        if not found and self.right:
            found, count = self.right._search(count, index)
        return found, count

    def __getitem__(self, index):
        found, _ = self._search(0, index)

        if not found:
            raise IndexError('Index out of range')
        return found.value


class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count


class BetterNode(SequenceNode, Sequence):
    pass


if __name__ == "__main__":
    pass
