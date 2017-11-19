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


class Deserialize(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Deserialize):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


if __name__ == "__main__":
    point = BetterPoint2D(5, 3)
    print('Before:', point)
    data = point.serialize()
    print('Serialized:', data)
    after = BetterPoint2D.deserialize(data)
    print('After:', after)
