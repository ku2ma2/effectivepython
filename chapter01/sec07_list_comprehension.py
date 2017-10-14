"""
項目7: mapやfilerの代わりにリスト内包表記を使う

リスト内包表記は余分な lambda式 を必要としないので明快な表記ができる
"""


def get_square(original: list):
    """
    入力されたリスト中の数を平方にして返す

    >>> get_square([1,2,3])
    [1, 4, 9]
    """

    return [x ** 2 for x in original]


def even_square(original: list):
    """
    入力されたリストの2で割れる数だけ平方にして返す

    >>> even_square([1,2,3,4])
    [4, 16]
    """

    return [x ** 2 for x in original if x % 2 == 0]


def len_chile_name(original: dict) -> dict:
    """
    与えられた辞書のキーの文字数を返す

    >>> len_chile_name({'moge': 3, 'lo': 10})
    {2, 4}
    """

    # ここをKeyとValueを逆順にするのは意味はないが例として・・・
    reverse_dict = {rank: name for name, rank in original.items()}

    # reverse_dict の値の文字列を新しい辞書に入れている
    len_set = {len(name) for name in reverse_dict.values()}

    return len_set


if __name__ == "__main__":
    pass
