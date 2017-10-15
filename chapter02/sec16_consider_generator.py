"""
項目16: リストを返さずにジェネレータを返すことを考える

Consider Generators Instead of Returning Lists

- リストを返す場合はジェネレータが使えないかを検討する、その方が明確になる場合がある
- ジェネレータが返すイテレータは、ジェネレータ関数の本体でyield式に渡される一連の値を生成する
- ジェネレータでは作業メモリに全ての入出力を保持しないので、ファイル読み込みなどの逐次実行に向いている(安全)
"""


def index_word_iter(text: str):
    """
    英文文字列(単語がスペースで区切られている)の各単語の位置をイテレータで返す

    >>> it = index_word_iter('Four score and seven years')
    >>> list(it)
    [0, 5, 11, 15, 21]
    """
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


if __name__ == "__main__":
    pass
