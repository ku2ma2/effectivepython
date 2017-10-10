"""
## 項目13: try/except/else/finallyの各ブロックを活用する

- try/finally 文では、tryブロックで例外が起きるかは関係なく必ず後処理を実行する
- elseは try記述を最小にして処理を分離して可読性をあげる
- elseは finallyの共通後処理前に追加作業をするのに便利
"""


def devide_json(names: list) -> str:
    """
    入力されたリスト内の一番長い文字列を返す

    >>> longest_name(['one','two','three'])
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
    print(devide_json())
