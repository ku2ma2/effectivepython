"""
項目29: 属性をリファクタリングする代わりに@propertyを考える

Consider @property Instead of Refactoring Attributes

- 

"""

import datetime


class Bucket(object):
    """
    水漏れバケツ
    """

    def __init__(self, period):
        """
        コンストラクタ
        """
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        """
        文字列表現を返す特殊関数、ここでは割当量を表示
        """
        return 'Bucket(quota={})'.format(self.quota)


if __name__ == "__main__":
    pass
