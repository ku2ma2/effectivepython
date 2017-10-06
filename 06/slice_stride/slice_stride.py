"""
項目6: 1つのスライスでは、start, end, strideを使わない

シーケンスって何を指しているのかがちょっと分からない。
恐らく list, str, bytesのようにリスト形式のものを包括的に
表現したのが「シーケンス」ではないかと。であればリストのスライスを詳しく知る
見たいな表現かもしれない。
"""


def get_slice_stride(slice_list, index: str = ''):
    """
    入力されたスライスを文字列表現されたインデックスを解釈して返す
    スライスの増分(stride)の

    >>> get_slice(['a','b','c'], '1:3:1')
    ['b','c']
    """

    indexes = index.split(':')
    key = []

    for i in range(3):
        if indexes[i]:
            key.append(int(indexes[i]))
        else:
            key.append(None)

    return slice_list[key[0]:key[1]:key[2]]


if __name__ == "__main__":
    print(get_slice_stride(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], '3:-3:2'))
