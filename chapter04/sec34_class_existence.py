"""
項目34: クラスの存在をメタクラスで登録する

Register Class Existence with Metaclasses

- 

### 所感

"""

import json


class Serializable(object):
    """
    JSONを独自でシリアライズする基底クラス
    """

    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)


if __name__ == "__main__":
    point = Point2D(5, 3)
    print('Object:', point)
    print('Serialized:', point.serialize())
