"""
## 項目10: rangeよりはenumerateにする

- リストの要素の添え字を利用する事があるが、rangeを使うより enumerateの方が自然
- enumerateはカウンタを開始する数も指定可能
"""


def convert_enumerate(origin: list, start: int = 0) -> list:
    """
    入力されたリストをインデックスを追加したタプルをリスト化して返す
    また、カウンタを開始する数 start を指定するとその数から開始する

    >>> convert_enumerate(['one','two','three'])
    [(0, 'one'), (1, 'two'), (2, 'three')]

    >>> convert_enumerate(['one','two','three'], 1)
    [(1, 'one'), (2, 'two'), (3, 'three')]
    """

    result = []
    for i, item in enumerate(origin, start):
        result.append((i, item))

    return result


if __name__ == "__main__":
    pass
