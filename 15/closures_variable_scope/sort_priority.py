"""
項目15: クロージャが変数スコープとどう関わるかを知っておく

Know How Closures Interact with Variable Scope

- 
"""


class Sorter(object):
    """
    sort関数で数をソートするための優先順位を返す、一部の数が優先するようにする
    直接実行された場合に蒸気が実行されてクロージャのように動作する
    また、一部の数自体が合致するかしないかをBoolで クラス変数 found
    に保存される

    >>> numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    >>> group = {2, 3, 5, 7}
    >>> sorter = Sorter(group)
    >>> numbers.sort(key=sorter)
    >>> sorter.found
    True
    >>> numbers
    [2, 3, 5, 7, 1, 4, 6, 8]
    """

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, check_list):
        if check_list in self.group:

            self.found = True
            return (0, check_list)
        return (1, check_list)
