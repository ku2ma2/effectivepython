"""
項目35: クラス属性をメタクラスで注釈する

Annotate Class Attributes with Metaclasses

- メタクラスは、クラスが完全に定義される前に、クラス属性を修正する事を可能にする。
- ディスクリプタとメタクラスとは、宣言的な振る舞いと実行時イントロスペクションのための強力なコンビ
- メタクラスをディスクリプタと一緒に使う事で、メモリリークとweakrefモジュールの両方を避けることができる

"""


class Field(object):
    """
    データベース行を表現したクラス
    """

    def __init__(self):
        """
        コンストラクタ
        属性名と内部属性名はメタクラスで代入される
        """
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    """
    属性名を毎度 Fieldに設定しなくても済むようにするメタクラス
    """
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    """
    メタクラス Meta を使うための基底クラス
    """
    pass


class BetterCustomer(DatabaseRow):
    """
    Field(行表現)を使った顧客データベースクラス

    >>> foo = BetterCustomer()
    >>> print('Before:', repr(foo.first_name), foo.__dict__)
    Before: '' {}

    >>> foo.first_name = 'Euclid'
    >>> print('After:', repr(foo.first_name), foo.__dict__)
    After: 'Euclid' {'_first_name': 'Euclid'}
    """
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


if __name__ == "__main__":
    pass
