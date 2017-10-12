"""
## 項目11: イテレータを並列に処理するにはzipを使う

- 組み込み関数zipが複数のイテレータを並列に処理するのに使える
- 異なる長さのイテレータを与えると、zipは何も言わずに出力を最短で止める
"""


def get_longest(names: list) -> str:
    """
    入力されたリスト内の一番長い文字列を返す

    >>> get_longest(['one','two','three'])
    'three'

    """

    letters = [len(n) for n in names]
    longest_name = None
    max_letters = 0

    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count

    return longest_name


if __name__ == "__main__":
    print(get_longest(['one', 'two', 'three']))
