"""
項目14: Noneを返すよりは例外を返す

Prefer Exceptions to Returning None

- Noneを返す事で何か意味を表す場合は 条件式に置いて Falseと認定されるのでエラーを呼びやすい
- Noneを返す代わりに例外を投げた方が契約的にも良さそう
"""


def devide(first: int, second: int) -> float:
    """
    除算するだけの関数
    0で割った場合の ZeroDivisionErrorは ValueErrorとして
    例外を再発生して返却する

    >>> devide(16, 8)
    2.0

    >>> devide(12, 0)
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    """

    try:
        return first / second

    except ZeroDivisionError as error:
        raise ValueError('Invalid input') from error


if __name__ == "__main__":
    pass
