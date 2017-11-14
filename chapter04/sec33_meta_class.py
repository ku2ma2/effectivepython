"""
項目33: サブクラスをメタクラスで検証する

Validate Subclasses with Metaclasses

- サブクラスの妥当性を、その型のオブジェクトが作られる前に検証するには、メタクラスを使う
- メタクラスは Python2 と Python3 で構文が少し異なる
- メタクラスは __new__ メソッドは、class文で本体全部が処理された後に実行される

### 所感

"""


class Meta(type):
    """
    DBの行(row)をPythonオブジェクトで表現する
    """

    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


if __name__ == "__main__":
    pass
