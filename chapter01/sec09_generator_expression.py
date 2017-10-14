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

    >>> line_num_and_square('my_file.txt')
    [(20, 400), (133, 17689), (151, 22801), (249, 62001), (73, 5329)]
    """

    result = []

    lines = []
    with open(my_file, mode='r', encoding='utf-8') as f:
        for row in f:
            lines.append(row.strip())

    word_numbers = (len(x) for x in lines)
    lists = ((x, x**2) for x in word_numbers)

    for item in lists:
        result.append(item)

    return result


if __name__ == "__main__":
    pass
    lists = line_num_and_square('sec09_file.txt')
    print(lists)
