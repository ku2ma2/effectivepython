"""
項目32: 遅延属性には __getattr__, __getattribute__, __setattr__ を使う

Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes

- デ

### 所感

"""


class LazyDB(object):
    """
    DBの行(row)をPythonオブジェクトで表現する

    >>> data = LazyDB()
    >>> print('Before:', data.__dict__)
    Before: {'exists': 5}
    >>> print('foo:', data.foo)
    foo: Value for foo
    >>> print('After:', data.__dict__)
    After: {'exists': 5, 'foo': 'Value for foo'}
    """

    def __init__(self):
        """
        """
        self.exists = 5

    def __getattr__(self, name):
        """
        """
        value = 'Value for %s' % name
        setattr(self, name, value)  # self.name = value と同じ意味
        return value


if __name__ == "__main__":
    pass
