"""
項目18: 可変長位置引数を使って見た目をすっきりさせる

Reduce Visual Noise with Variable Positional Arguments

- 関数で *argsを利用すると可変長引数を設定する事ができる
- *演算子を関数に用いて、シーケンスからの要素を可変長引数として使う事ができる
- 一度タプルに変換されるのでジェネレータを一緒に使うとメモリを使い果たしてしまう事がある
- *argsに設定されている関数に新たに引数を追加するときは発見困難なバグを生み出す可能性があるので注意する

"""


def log_with_arg(message, *values):
    """
    ログメッセージを表示する
    基本は message を出力して、可変長引数 *values は存在を
    する場合に文字列として連結をしたかたちで後ろに追加される

    >>> log_with_arg('My numbers are', 1, 2)
    My numbers are: 1, 2
    >>> log_with_arg('Hi there')
    Hi there
    """
    if not values:
        print(message)

    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


if __name__ == "__main__":
    pass
