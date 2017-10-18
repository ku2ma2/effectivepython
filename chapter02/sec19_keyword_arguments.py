"""
項目19: キーワード引数でオプションの振る舞いを表す

Provide Optional Behavior with Keyword Arguments

- 

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
