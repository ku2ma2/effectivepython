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


class LoggingLazyDB(LazyDB):
    """
    いつ __getattr__ が呼ばれたかのためにログ出力する
    LazyDBを継承して __getattr__ を上書きして実装

    >>> data = LoggingLazyDB()
    >>> print('exists:', data.exists)
    exists: 5
    >>> print('foo:', data.foo)
    Called __getattr__(foo)
    foo: Value for foo
    >>> print('foo:', data.foo)
    foo: Value for foo

    """

    def __getattr__(self, name):
        """
        いつ呼ばれたかをログ付きで表示
        super()を使う事で無駄な設定(書籍では無限再帰とか書かれてる)を避けている
        一度親の setattr() を設定する事で 何度も __getattr__が呼ばれないようにしている
        """
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


if __name__ == "__main__":
    pass
