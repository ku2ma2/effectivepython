"""
# 項目9: 大きな内包表記にはジェネレータ式を考える

- 大きな内包表記はファイルから読み込んだりした場合メモリを圧迫するので使わない
- 代わりにジェネレータ式を使うことによって回避できる
- さらにジェネレーター式を組み合わせる事も可能
"""


def line_num_and_square(my_file: str) -> list:
    """
    入力されたファイル名のファイルから文字数とその文字数の二乗を返す

    ファイル名(my_file.txt)の内容が以下だった場合
    This is a pen
    Hello, world
    以下のように(文字数, 文字数**2)のタプルを行数分リスト化して返る
    最後の改行も文字に含まれる(rstripしても良いかも…)

    >>> line_num_and_square('my_file.txt')
    [(14, 196), (13, 169)]
    """

    result = []
    word_numbers = (len(x) for x in open(my_file))
    lists = ((x, x**2) for x in word_numbers)

    for item in lists:
        result.append(item)

    return result


if __name__ == "__main__":
    lists = line_num_and_square('my_file.txt')
    print(lists)
