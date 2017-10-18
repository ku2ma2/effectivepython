"""
項目18: 可変長位置引数を使って見た目をすっきりさせる

Reduce Visual Noise with Variable Positional Arguments

- a
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
