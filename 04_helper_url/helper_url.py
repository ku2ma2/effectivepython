"""
項目4: 複雑な式の代わりにヘルパー関数を書く

複雑であり、暗黙的なFalseを利用しての三項演算子などを利用する位なら
ヘルパー関数を実装しましょう。という趣旨
"""
from urllib.parse import parse_qs


def get_first_int(values: dict, key: str, default: int =0):
    """
    辞書からデフォルトを指定しつつ値を取り出す
    values 辞書から key キーで値を取り出し、値がない場合などは default 
    の値を利用する

    >>> m = get_first_int({'key':'value'}, 'nokey', 5)
    >>> print(m) # => 5
    """
    return values.get(key)


def main():
    """
    URLクエリー文字列を復元したい場合
    """
    url_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
    print("Red: {}".format(get_first_int(url_values, 'red')))
    print("Green: {}".format(get_first_int(url_values, 'green')))
    print("Opacity: {}".format(get_first_int(url_values, 'opacity')))


if __name__ == "__main__":
    main()
