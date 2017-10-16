"""
項目17: 引数に対してイテレータを使うときは確実さを尊ぶ

Be Defensive When Iterating Over Arguments

- 日本語版書籍の翻訳に関してネガティブな意見がネットで確認したが何となくわかってきた。日本語が分かりづらい…。
"""


def normalize_defensive(numbers):
    """
    数値リスト numbers の総計と其々の値のパーセンテージをリストにして返す

    >>> numbers = [15, 35, 80]
    >>> normalize_defensive(numbers)
    [11.538461538461538, 26.923076923076923, 61.53846153846154]
    """
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


class ReadVisits(object):
    """
    ファイルを読み込み、各行を数値にした上で返す。
    イテレータで呼ばれる事を想定しており、行単位でyieldで返す
    """

    def __init__(self, data_path):
        """ コンストラクタ
        """
        self.data_path = data_path

    def __iter__(self):
        """ イテレータマジックメソッド
        """
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


if __name__ == "__main__":
    visits = ReadVisits('sec17_test.txt')
    percentages = normalize_defensive(visits)
    print(percentages)
