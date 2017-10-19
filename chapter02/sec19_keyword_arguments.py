"""
項目19: キーワード引数でオプションの振る舞いを表す

Provide Optional Behavior with Keyword Arguments

- 関数の引数は、位置またはキーワードによって指定可能
- キーワード引数は、位置引数だけでは紛らわしい場合に、各引数の目的を明確にする
- デフォルト値を設定したキーワード引数は、関数が別の場所に使われている状態でも新たな振る舞いを追加する事を容易にする
- オプション(あってもなくても良い)のキーワード引数は位置ではなくキーワードで常に渡すべきである
"""


def remainder(number, division):
    """
    単純に剰余を返す関数

    >>> remainder(20, 7)
    6
    >>> remainder(20, division=7)
    6
    >>> remainder(number=20, division=7)
    6
    >>> remainder(division=7, number=20)
    6
    >>> remainder(number=20, 7)
    Traceback (most recent call last):
    ...
    SyntaxError: positional argument follows keyword argument

    >>> remainder(20, number=7)
    Traceback (most recent call last):
    ...
    TypeError: remainder() got multiple values for argument 'number'
    """
    return number % division


if __name__ == "__main__":
    pass
