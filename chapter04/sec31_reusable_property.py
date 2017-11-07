"""
項目31: ディスクリプタを使って @property デコレータのメソッドを再利用可能にする

Use Descriptors for Reusable @property Methods

- ディスクリプタを定義して、@property メソッドの振る舞いや確認作業を再利用する
- WeakKeyDirectoryを用いて、ディスクリプタクラスがメモリリークを起こさないようにする
- __getattribute__ がディスクリプタプロトコルをどのように使って属性の取得や設定を行なっているか、正確に把握しようとして立ち往生をしない。

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
    bucket = Bucket(period=60)
    fill(bucket, 100)
    print(bucket)
    if deduct(bucket, 99):
        print('Had 99 quota')
    else:
        print('Not enough for 99 quota')
    print(bucket)
