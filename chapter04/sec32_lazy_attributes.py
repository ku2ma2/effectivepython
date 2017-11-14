"""
項目32: 遅延属性には __getattr__, __getattribute__, __setattr__ を使う

Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes

- オブジェクトの属性を遅延的にロードしたり保存したりするには、__getattr__と__setattr__を使う
- __getattr__は見つからない属性にアクセスするときに一度だけ呼び出され、__getattribute__は
属性がアクセスされるたびに呼び出される
- super() (すなわちobjectクラス)のメソッドを使ってインスタンス属性に直接アクセスする事で、
__getattribute__ と __ setattr__とで無限再帰に入るのを防ぐ

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


class ValidatingDB(object):
    """
    データベーストランザクションを想定した属性設定のパターン

    >>> data = ValidatingDB()
    >>> print('exists:', data.exists)
    Called __getattribute__(exists)
    exists: 5

    >>> print('foo:', data.foo)
    Called __getattribute__(foo)
    foo: Value for foo
    >>> print('foo:', data.foo)
    Called __getattribute__(foo)
    foo: Value for foo
    """

    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        """
        上記 __getattr__ だと毎回呼ばれないが、データベースのトランザクションが
        オープンかどうかのチェックなど「毎回」実行したい場合は __getattribute__
        を利用する
        """
        print('Called __getattribute__(%s)' % name)

        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


class SavingDB(object):
    def __stattr__(self, name, value):
        # DBログにデータを残す処理 -- 想定 --
        super().__setattr__(name, value)


class LoggingSavingDB(SavingDB):
    """
    ロギングを追加したDBデータ追加処理

    >>> data = LoggingSavingDB()
    >>> print('Before:', data.__dict__)
    Before: {}
    >>> data.foo = 5
    Called __setattr__(foo, 5)
    >>> print('After:', data.__dict__)
    After: {'foo': 5}
    >>> data.foo = 7
    Called __setattr__(foo, 7)
    >>> print('Finally:', data.__dict__)
    Finally: {'foo': 7}
    """

    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)


class DirectoryDB(object):
    """
    __getattribute__のオブジェクト属性アクセス

    >>> data = DirectoryDB({'foo': 3})
    >>> data.foo
    3
    """

    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


if __name__ == "__main__":
    pass
