"""
項目30: 属性をリファクタリングする代わりに @property を考える

Consider @property Instead of Refactoring Attributes

- 例題は リーキーバケット https://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%BC%E3%82%AD%E3%83%BC%E3%83%90%E3%82%B1%E3%83%83%E3%83%88
- @propertyを使って既存のインスタンス属性に新たな機能を与える
- @propertyを使って、より良いデータモデルへ逐次改善する
- @propertyをあまり使いすぎるようになったら、そのクラスと全ての呼び出し元をリファクタリングする事を考える

"""

from datetime import datetime, timedelta


class Bucket(object):
    """
    水漏れバケツ
    """

    def __init__(self, period):
        """
        コンストラクタ
        """
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        """
        Pythonの文字列表現を返す特殊関数、ここでは割当量を表示
        """
        return ('Bucket(max_quota=%d, quota_consumed=%d)' % (self.max_quota, self.quota_consumed))

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount

        if amount == 0:
            # 新たなピリオドのための割当量をリセット
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 新たなピリオドのための割当量を入れる
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # ピリオド内で割当量が消費される
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


if __name__ == "__main__":
    pass
