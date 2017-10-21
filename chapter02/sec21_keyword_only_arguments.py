"""
項目21: キーワード専用引数で明確さを高める

Enforce Clarity with Keyword-Only Arguments

- 関数の引
"""

from datetime import datetime


def safe_division(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    """
    除算するだけの関数だが通常想定されないような場合も対処するようにする。
    結果がFloatをオーバーフローした場合 -> ignore_overflow が True ならば 0 を返す
    0で除算 -> ignore_zero_division が True ならば inf(無限大) を返す
    中央の「*」がキモで、なくても良くても良いけど後ろに続くのはキーワード引数として
    扱わないといけないという事を強制している

    Args:
        number, divisor: 除算する数
        ignore_overflow: 結果がオーバーフローしても強制的に処理
        ignore_zero_division: 0で除算して例外になっても強制的に処理

    >>> # ignore_zero_divisionを設定
    >>> safe_division(1.0, 10**500, ignore_overflow=True, \
    ignore_zero_division=False)
    0
    >>> # ignore_zero_division を設定
    >>> safe_division(1.0, 0, ignore_overflow=False, ignore_zero_division=True)
    inf
    >>> # キーワード引数を設定しないとエラー
    >>> safe_division(1.0, 10**500, True)
    Traceback (most recent call last):
    ...
    TypeError: safe_division() takes 2 positional arguments but 3 were given
    """

    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise

    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


if __name__ == "__main__":
    pass
