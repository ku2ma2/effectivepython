"""
項目33: サブクラスをメタクラスで検証する

Validate Subclasses with Metaclasses

- サブクラスの妥当性を、その型のオブジェクトが作られる前に検証するには、メタクラスを使う
- メタクラスは Python2 と Python3 で構文が少し異なる
- メタクラスは __new__ メソッドは、class文で本体全部が処理された後に実行される

### 所感

- このValidatePolygonのテストはどうやってやるんだろうか…

"""


class ValidatePolygon(type):
    """
    多角形表現を検証するメタクラス
    """

    def __new__(meta, name, bases, class_dict):
        """
        インスタンス作成時に呼び出される
        """
        # ここで妥当性を検査して Polygonでは行わない
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygon need 3+ sides')

        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    """
    多角形(Polygon)の抽象クラス
    """
    sides = None  # サブクラスで決定する

    @classmethod
    def interior_angles(cls):
        """
        内角の和
        """
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    """
    三角形クラス
    """
    sides = 3


if __name__ == "__main__":
    pass
