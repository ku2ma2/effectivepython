"""
項目29: getやsetメソッドよりもの素のままの属性を使う

Use Plain Attributes Instead of Get and Set Methods

- getterやsetterではなく単純なパブリックな属性にアクセスする。
- 属性にアクセスされた時に特別な振る舞いが必要なのであれば @property を使って定義する
- 驚き最小の原則を守り、 @property メソッドで奇妙な副作用が生じるのを防ぐ
- 上記は他属性を変更するのは注意が必要という主旨で、「getter, setter使うな論」と同じような事を言ってる。
- @propertyメソッドが高速な事を確かめる。遅かったり、複雑になったりする作業は通常のメソッドを使う

"""


class Resistor():
    """
    抵抗器
    """

    def __init__(self, ohms):
        """
        コンストラクタ

        >>> r1 = Resistor(50e3)
        >>> r1.ohms = 10e3
        >>> r1.ohms
        10000.0
        """
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    """
    抵抗器のボルト計算
    """

    def __init__(self, ohms):
        """ コンストラクタ
        """
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        """
        voltage getter関数
        @propertyデコレータを使って getter的な振る舞いを作る
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """
        voltage setter関数
        @setterデコレータを使って getter的な振る舞いを作る
        """
        self._voltage = voltage
        self.current = self._voltage / self.ohms


class BoundedResistance(Resistor):
    """
    抵抗器のオーム計算
    """

    def __init__(self, ohms):
        """ コンストラクタ
        """
        super().__init__(ohms)

    @property
    def ohms(self):
        """
        ohms getter関数
        @propertyデコレータを使って ohms的な振る舞いを作る
        """
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """
        ohms setter関数
        @setterデコレータを使って getter的な振る舞いを作る
        設定された ohms が0以下であった場合は ValueErrorの例外
        """
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


class FixedResistance(Resistor):
    """
    抵抗器のオーム計算
    """

    def __init__(self, ohms):
        """ コンストラクタ
        """
        super().__init__(ohms)

    @property
    def ohms(self):
        """
        ohms getter関数
        @propertyデコレータを使って ohms的な振る舞いを作る
        """
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """
        ohms setter関数
        @setterデコレータを使って getter的な振る舞いを作る
        インスタンスで初期化後に再度代入しようとするとAttributeError
        """
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


if __name__ == "__main__":
    pass
