"""
項目4: シーケンスをどのようにスライスするか知っておく

シーケンスって何を指しているのかがちょっと分からない。
恐らく list, str, bytesのようにリスト形式のものを包括的に
表現したのが「シーケンス」ではないかと。であればリストのスライスを詳しく知る
見たいな表現かもしれない。
"""


def get_slice(slice_list, index: str = ''):
    """
    入力されたスライスを文字列表現されたインデックスを解釈して返す

    >>> get_slice(['a','b','c'], '1:3')
    ['b', 'c']
    """

    indexes = index.split(':')
    start = None
    end = None

    if indexes[0]:
        start = int(indexes[0])

    if indexes[1]:
        end = int(indexes[1])

    return slice_list[start:end]


if __name__ == "__main__":
    pass
