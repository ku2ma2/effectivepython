"""
項目15: クロージャが変数スコープとどう関わるかを知っておく

Know How Closures Interact with Variable Scope

- 
"""


def sort_priority(values: list, group: set):
    """
    除算するだけの関数
    0で割った場合の ZeroDivisionErrorは ValueErrorとして
    例外を再発生して返却する

    >>> devide(16, 8)
    2.0

    >>> devide(12, 0)
    ValueException

    """

    def helper(key):
        if key in group:
            return (0, key)
        return (1, key)

    values.sort(key=helper)


if __name__ == "__main__":
    print(sort_priority(16, 8))
